from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response


class TodoView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        pass


class TodoDetailView(APIView):
    def get(self, request, todo_id):
        pass

    def put(self, request, todo_id):
        pass

    def delete(self, request, todo_id):
        pass


class StatusView(APIView):
    def post(self, request):
        pass
