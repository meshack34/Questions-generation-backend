from django.urls import path
from .views import RegisterView, LoginView, GenerateQuestionsView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('generate-questions/', GenerateQuestionsView.as_view(), name='generate_questions'),
]
