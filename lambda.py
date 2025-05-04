import boto3
import botocore.config
import json


def remedy_generate_using_bedrock(health_problem:str)-> str:
    prompt = f"""<s>[INST]Human: I am facing a minor health issue: {health_problem}. 
    Please provide possible suggestions including:
    - Over-the-counter medicines (with dosage if applicable)
    - Simple home remedies
    - Prevention tips to avoid this issue in the future.
    Keep the response concise, factual, and suitable for general guidance (not a substitute for professional medical advice).
    Assistant:[/INST]
"""

    body = {
    "inferenceConfig": {
        "max_new_tokens": 512,
        "temperature": 0.5,
        "top_p": 0.9
    },
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "text": prompt  # this is your user input
                }
            ]
        }
    ]
}


    try:
        bedrock=boto3.client("bedrock-runtime",region_name="us-east-1",
                             config=botocore.config.Config(read_timeout=300,retries={'max_attempts':3}))
        response=bedrock.invoke_model(body=json.dumps(body),modelId="amazon.nova-lite-v1:0")

        response_content=response.get('body').read()
        response_data=json.loads(response_content)
        print(response_data)
        remedy_details=response_data['generation']
        return remedy_details
    except Exception as e:
        print(f"Error generating the remedy:{e}")
        return ""

def save_remedy_details_s3(s3_key,s3_bucket,generate_remedy):
    s3=boto3.client('s3')

    try:
        s3.put_object(Bucket = s3_bucket, Key = s3_key, Body =generate_remedy )
        print("Code saved to s3")

    except Exception as e:
        print("Error when saving the code to s3")



def lambda_handler(event, context):
    # TODO implement
    event=json.loads(event['body'])
    health_problem=event['issue_topic']

    generate_remedy=remedy_generate_using_bedrock(health_problem=health_problem)

    if generate_remedy:
        s3_key=f"output.txt"
        s3_bucket='awsbedrockapps'
        save_remedy_details_s3(s3_key,s3_bucket,generate_remedy)

    else:
        print("No remedy was generated")

    return{
        'statusCode':200,
        'body':json.dumps('Remedy Generation is completed')
    }

    



