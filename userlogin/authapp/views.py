from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Project, Skill, Achievement, ContactForm
from .serializers import (
    UserLoginSerializer,
    ProjectSerializer,
    SkillSerializer,
    AchievementSerializer,
    ContactFormSerializer,
)


class LoginView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                return Response(
                    {
                        "success": True,
                        "message": "Login successful",
                        "access": str(refresh.access_token),
                        "refresh": str(refresh),
                    },
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"success": False, "message": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {"success": True, "message": "Logout successful"},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {"success": False, "message": "Invalid token"},
                status=status.HTTP_400_BAD_REQUEST,
            )

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [IsAuthenticated]

class ContactFormViewSet(viewsets.ModelViewSet):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
