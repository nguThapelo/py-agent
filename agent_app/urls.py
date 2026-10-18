from django.urls import path
from .views import index, ask_tutor

urlpatterns = [
    path('', index, name='index'),
    path('api/ask/', ask_tutor, name='ask_tutor'),
]
