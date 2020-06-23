from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    # 과거에 작성한 글을 불러와 게시일 기준으로 정렬하는 쿼리셋을 변수 posts에 할당
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # 'reqeust'를 넘겨 받아 'render' 함수를 호출하고, 함수는 'blog/post_list.html' 템플릿 출력, 매개변수로서 쿼리셋 posts 받기
    return render(request, 'blog/post_list.html', {'posts': posts})

# 블로그 한 개의 상세 페이지를 보기 위해 요청과 식별값(pk)을 매개변수로 받는다
def post_detail(request, pk):
    # 식별값이 pk인 Post를 불러와 변수에 저장한다
    post = get_object_or_404(Post, pk=pk)
    # 해당 템플릿에 post를 매개변수로 전달하고 불러온다
    return render(request, "blog/post_detail.html", {"post": post})