from django.urls import path
from .views import index, ask_agent

urlpatterns = [
    path('', index, name='index'),
    path('api/ask/', ask_agent, name='ask_agent'),
]
