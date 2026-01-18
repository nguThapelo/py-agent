from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from agents.simple_search import generate_response

def index(request):
    """Render the main page."""
    return render(request, "index.html")

@api_view(['POST'])
def ask_agent(request):
    query = request.data.get("query", "")
    try:
        response = generate_response(user_message=query)
        # Limit message to 200 characters
        message = response.message
        if len(message) > 200:
            message = message + "..."
        return Response({"message": message})
    except Exception as e:
        return Response({"error": str(e)})
