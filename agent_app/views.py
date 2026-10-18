from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response

from agents.tutor import GRADES, SUBJECTS, get_tutor, sanitize_messages


def index(request):
    """Render the tutor page."""
    return render(request, "index.html", {"grades": GRADES, "subjects": SUBJECTS})


@api_view(["POST"])
@authentication_classes([])
def ask_tutor(request):
    """Stateless: the browser sends the recent conversation, nothing is stored."""
    grade = str(request.data.get("grade", ""))
    subject = request.data.get("subject", "")
    messages = sanitize_messages(request.data.get("messages"))

    if grade not in GRADES or subject not in SUBJECTS or not messages:
        return Response({"error": "Please choose a grade and subject, then type a question."}, status=400)

    try:
        return Response(get_tutor().reply(grade, subject, messages))
    except Exception:
        return Response({"error": "The tutor is unavailable right now. Please try again."}, status=503)
