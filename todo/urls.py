# from django.urls import path
# from . import views

# app_name ="todo"

# urlpatterns = [
# 	# path("list/", views.todo_list, name="list"), # 첫 테스트용
# 	path("list/", views.TodoListView.as_view(), name="list"),

# ]
from django.urls import path
from .views.templates_views import TodoListView, TodoCreateView, TodoDetailView
from .views.api_views import TodoListAPI, TodoCreateAPI, TodoRetrieveAPI, TodoUpdateAPI

app_name = "todo"

# urlpatterns = [
#     # path("list/", views.todo_list, name="todo_List"), # 첫 테스트용
#     path("list/", TodoListView.as_view(), name="list"),

#     # api
#     path("api/list/", TodoListAPI.as_view(), name="todo_api_list"),
# ]

urlpatterns = [
    # path("list/", views.todo_list, name="todo_List"), # 첫 테스트용
    # HTML 렌더링 뷰
    path("list/", TodoListView.as_view(), name="list"),
    path("create/", TodoCreateView.as_view(), name="todo_create"),
    path("detail/<int:pk>/", TodoDetailView.as_view(), name="todo_Detail"),
    # api DRF / JSON 응답 뷰
    path("api/list/", TodoListAPI.as_view(), name="todo_api_list"),
    path("api/create/", TodoCreateAPI.as_view(), name="todo_api_create"),
    path("api/retrieve/<int:pk>/", TodoRetrieveAPI.as_view(), name="todo_api_retrieve"),
    path("api/update/<int:pk>/", TodoUpdateAPI.as_view(), name="todo_api_update"),
]
