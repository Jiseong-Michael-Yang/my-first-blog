from django.shortcuts import render

# Create your views here.
def post_list(request):
    # 'reqeust'를 넘겨 받아 'render' 함수를 호출하고, 함수는 'blog/post_list.html' 템플릿 출력
    return render(request, 'blog/post_list.html', {})