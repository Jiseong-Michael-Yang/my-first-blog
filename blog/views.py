from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    # 과거에 작성한 글을 불러와 게시일 기준으로 정렬하는 쿼리셋을 변수 posts에 할당
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # 'reqeust'를 넘겨 받아 'render' 함수를 호출하고, 함수는 'blog/post_list.html' 템플릿 출력, 쿼리셋은 posts 받기
    return render(request, 'blog/post_list.html', {'posts': posts})