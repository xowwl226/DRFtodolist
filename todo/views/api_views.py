# DRF ViewSet 사용
from rest_framework import viewsets

# 인증된 사용자만 접근 가능하도록 하는 권한 클래스
from rest_framework.permissions import IsAuthenticated

# 페이지네이션 기능
from rest_framework.pagination import PageNumberPagination

# Todo 모델
from ..models import Todo

# Todo 데이터를 JSON으로 변환하는 Serializer
from ..serializers import TodoSerializer


# ---------------------------------------
# Todo 목록 페이지네이션 설정
# ---------------------------------------
class TodoListPagination(PageNumberPagination):

    # 기본 페이지당 데이터 개수
    page_size = 3

    # URL에서 page_size를 변경할 수 있도록 허용
    # 예: /api/todos/?page_size=10
    page_size_query_param = "page_size"

    # 최대 페이지 크기 제한
    max_page_size = 50


# ---------------------------------------
# Todo ViewSet
# ---------------------------------------
class TodoViewSet(viewsets.ModelViewSet):

    # Todo 데이터를 변환할 Serializer 지정
    serializer_class = TodoSerializer

    # 로그인한 사용자만 API 접근 가능
    permission_classes = [IsAuthenticated]

    # 페이지네이션 설정 적용
    pagination_class = TodoListPagination

    # 조회할 queryset 설정
    def get_queryset(self):

        # 현재 로그인한 사용자(request.user)의 Todo만 조회
        # 최신 Todo가 먼저 나오도록 created_at 기준 내림차순 정렬
        return Todo.objects.filter(user=self.request.user).order_by("-created_at")

    # Todo 생성 시 실행되는 메서드
    def perform_create(self, serializer):

        # Todo 생성할 때 현재 로그인한 사용자를 자동으로 user 필드에 저장
        serializer.save(user=self.request.user)
