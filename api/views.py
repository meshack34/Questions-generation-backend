from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, QuestionSerializer
from .models import Question

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': str(token)}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class GenerateQuestionsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        text_content = request.data.get('textContent')
        question_type = request.data.get('questionType')
        user = request.user
        question = Question.objects.create(
            text_content=text_content,
            question_type=question_type,
            user=user
        )
        serializer = QuestionSerializer(question)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
