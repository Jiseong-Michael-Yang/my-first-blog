from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

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

def post_new(request):
    # 폼을 저장하는 방식이 POST인 경우
    if request.method == "POST":
        # request.POST에 저장된 데이터를 폼에 넘겨주기
        form = PostForm(request.POST)
        # 폼에 들어간 값들이 올바른지 확인 (모든 필드에는 값이 있어야 하고 잘못된 값이 있다면 저장되지 않아야 한다)
        if form.is_valid():
            # 폼 저장
            post = form.save(commit=False) # commit-False: 이어서 작성자 데이터를 저장해야하니 넘겨진 데이터를 바로 Post 모델에 저장하지 말 것
            # 작성자 추가
            post.author = request.user
            # 작성일 추가
            post.published_date = timezone.now()
            # 변경사항을 유지하고 저장
            post.save()
            # 해당 pk값에 해당하는 글 상세 페이지로 리다이렉트
            return redirect('post_detail', pk=post.pk)
    # 폼을 저장하는 방식이 POST가 아닌 경우
    else:
        # 폼을 생성하되 값을 보내지 않기
        form = PostForm()
    # form이 매개변수로 넘겨진 템플릿 파일 열기
    return render(request, "blog/post_edit.html", {"form": form})

# 폼을 수정하기 때문에 해당 게시물의 pk값을 매개변수로 받는다
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post) # 수정하고자 하는 글을 pk로 찾고 Post 모델을 인스턴스로 가져옴
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("post_detail", pk=post.pk)
    # 새로 작성한 글이 아니기 때문에 request.POST가 아니라 instance로서 post를 보내준다
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_edit.html", {"form": form})