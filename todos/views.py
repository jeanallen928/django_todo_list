from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from todos.models import Todo
from todos.serializers import TodoSerializer, TodoCreateSerializer


class TodoView(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TodoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


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
