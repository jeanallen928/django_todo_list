from django.urls import path
from todos import views


urlpatterns = [
    path('', views.TodoView.as_view(), name="todo_view"),
    path('<int:todo_id>/', views.TodoDetailView.as_view(), name="todo_detail_view"),
    path('status/', views.StatusView.as_view(), name="status_view"),
]
