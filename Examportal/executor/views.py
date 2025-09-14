from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .services import run_user_code


@csrf_exempt
def execute_code(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        code = data.get("code")
        language = data.get("language", "python")

        if not code:
            return JsonResponse({"error": "No code provided"}, status=400)

        try:
            result = run_user_code(code, language)
            return JsonResponse({"result": result})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)
