from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,logout
from .serializers import UserLoginSerializer

class LoginView(APIView):
    authentication_classes = []  
    permission_classes = []      

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                # Token yaratmadan sadəcə uğurlu cavab qaytar
                return Response({
                    "success": True,
                    "message": "Login successful"
                }, status=status.HTTP_200_OK)
            return Response({"success": False, "message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    authentication_classes = [] 
    permission_classes = []     

    def post(self, request):
        logout(request)
        return Response({"success": True, "message": "Logout successful"}, status=status.HTTP_200_OK)