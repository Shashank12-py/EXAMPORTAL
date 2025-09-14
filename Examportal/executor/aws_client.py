import boto3
import json
import os


def invoke_lambda(code: str, language: str = "python"):
    """
    Invoke AWS Lambda function to execute user code.
    Expects Lambda function to accept { "code": ..., "language": ... }.
    """
    client = boto3.client(
        "lambda",
        region_name=os.getenv("AWS_REGION", "us-east-1")
    )

    payload = {"code": code, "language": language}

    response = client.invoke(
        FunctionName=os.getenv("LAMBDA_FUNCTION_NAME"),
        InvocationType="RequestResponse",
        Payload=json.dumps(payload),
    )

    result = json.load(response["Payload"])
    return result
