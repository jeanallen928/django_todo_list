from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from todos.models import Todo
from todos.serializers import TodoSerializer, TodoCreateSerializer


class TodoView(APIView):
    def get(self, request):
        todos = Todo.objects.filter(user=request.user).order_by('-created_at')
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TodoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailView(APIView):
    def get(self, request, todo_id):
        todo = get_object_or_404(Todo, id=todo_id)
        if request.user == todo.user:
            serializer = TodoSerializer(todo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)

    def put(self, request, todo_id):
        todo = get_object_or_404(Todo, id=todo_id)
        if request.user == todo.user:
            serializer = TodoCreateSerializer(todo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, todo_id):
        todo = get_object_or_404(Todo, id=todo_id)
        if request.user == todo.user:
            todo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)


class StatusView(APIView):
    def post(self, request):
        pass
