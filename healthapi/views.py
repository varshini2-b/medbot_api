from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def chat_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_input = data.get("message", "").lower()

            # BASIC BOT LOGIC:
            if "headache" in user_input:
                response = "Drink water and rest. If it continues, consult a doctor."
            elif "fever" in user_input:
                response = "Monitor your temperature and take paracetamol if needed."
            else:
                response = "I didn't understand. Can you describe your symptoms again?"

            return JsonResponse({"response": response})
        
        except Exception as e:
            return JsonResponse({"error": str(e)})

    return JsonResponse({"message": "Send a POST request with a 'message' field."})




