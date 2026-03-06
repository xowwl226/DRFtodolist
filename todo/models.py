# # from django.db import models


# # class Todo(models.Model):
# #     name = models.CharField(max_length=100)
# #     description = models.TextField(blank=True)
# #     complete = models.BooleanField(default=False)
# #     exp = models.PositiveIntegerField(default=0)
# #     completed_at = models.DateTimeField(null=True, blank=True)
# #     created_at = models.DateTimeField(auto_now_add=True)
# #     updated_at = models.DateTimeField(auto_now=True)

# #     def __str__(self):
# #         return self.name
# from rest_framework.serializers import ModelSerializer
# from .models import Todo

# # API 요청 데이터를 모델 객체로 변환하는 변환기
# class TodoSerializer(ModelSerializer):
#     class Meta:
#         model = Todo
#         fields = "__all__" # 모델의 모든 필드를 자동으로 직렬화합니다.
#         read_only_fields = ["created_at", "updated_at"] # 읽기만 가능


#         fields = [
#             "name",
#             "description",
#             "complete",
#             "exp",
#             "completed_at",
#             "created_at",
#             "updated_at"
#         ]


#         exclude = ["created_at", "updated_at"]
#         # 모든 필드를 기본 포함시키고 → 특정 필드만 제외하고 싶을 때

# # 둘중 한개를 사용합니다.
from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    exp = models.PositiveIntegerField(default=0)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
