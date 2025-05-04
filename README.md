# 🩺 AI-Based Remedy Suggestion using AWS Bedrock

## 📌 Aim of the Project

To build an intelligent, serverless application that provides possible remedies (medications, home treatments, and prevention tips) for **minor health issues** using **Amazon Bedrock's GenAI models**.

---

## 📝 Project Description

This project accepts a user input like `"headache"` or `"stomach pain"` and returns:

- Over-the-counter medicines (with dosage if applicable)
- Simple home remedies
- Prevention tips for the future

The backend is powered by **Amazon Bedrock's `amazon.nova-lite-v1:0` model**, integrated into a serverless Lambda function that generates responses in real-time and saves the output to an **S3 bucket**.

---

## 🛠️ Tools & Technologies Used

- **AWS Lambda**: For executing remedy generation logic.  
  - A Lambda **layer** was attached containing the required packages using{Hint:- Refer script.py}:
    ```bash
    pip install boto3 -t python/
    ```
- **Amazon S3**: For storing generated remedy text files.
- **Amazon Bedrock**: For invoking GenAI model (`amazon.nova-lite-v1:0`).
- **Amazon API Gateway**: For exposing the Lambda function as a public REST API.
- **Postman**: To trigger and test API requests.
- **AWS CloudWatch**: For logging and monitoring API responses and Lambda behavior.
- **Python (boto3, json)**: Core programming language for the logic.

---

## 📈 Inference / Conclusion

- This system demonstrates how **Generative AI** can be used responsibly to deliver **general health advice**.
- The solution is **cost-effective**, **scalable**, and **fully serverless**.
- Successfully integrates AWS services for real-world applications like symptom-based health recommendations.

---

## 🚀 Further Enhancements Possible

- ✅ Integrate authentication to validate request origin (using Cognito or API keys).
- ✅ Add multilingual support for remedy suggestions.
- ✅ Enhance responses by connecting to medical APIs like WebMD or MedlinePlus.
- ✅ Cache previous responses for recurring queries (using DynamoDB).
- ✅ Add a front-end UI using React or Streamlit for better user interaction.

---

## 📂 Sample Prompt Format

```python
prompt = f"""<s>[INST]Human: I am facing a minor health issue: {health_problem}. 
Please provide possible suggestions including:
- Over-the-counter medicines (with dosage if applicable)
- Simple home remedies
- Prevention tips to avoid this issue in the future.
Keep the response concise, factual, and suitable for general guidance (not a substitute for professional medical advice).
Assistant:[/INST]"""


![App Screenshot](screenshots.assistant_response)
