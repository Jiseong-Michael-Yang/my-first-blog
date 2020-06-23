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
        name="post_list"),
    # mysite.urls에서 /admin외의 모든 값("")은 blog.urls에서 찾으라고 했다
    path(
        # 장고가 아래 규칙의 URL을 받으면 (정수인 pk 값)
        "post/<int:pk>/", \
        # post_detail 뷰로 보내 게시글이 보일 수 있게 함
        views.post_detail, \
        # 장고가 post_detail이라는 이름을 해석할 때 blog/views.py 내부의 post_detail 함수로 이해
        name="post_detail")
]