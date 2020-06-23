# 장고 함수 path와 app에서 사용할 모든 views 가져오기
from django.urls import path
from . import views

urlpatterns = [
    path(
        # 빈 문자열에 매칭되어 접두어에 포함되는 도메인 이름(http://127.0.0.1:8000/) 무시
        "", \
        # http://127.0.0.1:8000/로 들어왔을 때 views.post_list 보여주기
        views.post_list, \
        # URL 이름으로서 view를 식별
        name="post_list")
]