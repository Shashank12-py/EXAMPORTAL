from .aws_client import invoke_lambda


def run_user_code(code: str, language: str = "python"):
    """
    Send user code to AWS Lambda and return result.
    """
    return invoke_lambda(code, language)