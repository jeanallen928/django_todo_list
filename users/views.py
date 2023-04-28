from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import logout
from users.models import User

from users.serializers import UserSerializer, CustomTokenObtainPairSerializer

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "가입완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class mockView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        print(request.user)
        return Response("로그인 확인")


class InfoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        request.user.delete()
        logout(request)
        return Response({"message": "회원 탈퇴!"})


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        response = Response({
            "message": "로그아웃 성공!"
        }, status=status.HTTP_202_ACCEPTED)
        response.delete_cookie("refresh")
        return response
