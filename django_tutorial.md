# Django Tutorial


## 1. 가상환경 만들기
1. 디렉토리 생성
   * `mkdir django_toturial`
2. 가상환경 생성 및 실행
    * `python3 -m venv tutorial`
    * `tutorial\Scripts\activate`

## 2. Django 설치
1. `pip` 업데이트
    * `python -m pip install --upgrade pip`
2. Django 설치
   * `pip install django~=2.0.0` 

## 3. 프로젝트 만들기
1. 장고의 기본 골격만들기
   * 명령줄: `django-admin startproject mysite .`
2. `mysite/settings.py` 변경
    * `TIME_ZONE` 변경
    * `STATIC_ROOT = os.path.join(BASE_DIR, 'static')`: 정적파일 경로 추가
    * `ALLOWED_HOSTS` 변경
3. 데이터베이스 설정
   * `sqlite31`이미 `mysite/settings.py`에 이미 설치
   * `python manage.py migrate`: 블로그에 데이터베이스를 생성 (`manage.py`를 통해 변경사항 저장)
4. 서버 실행
   * `python manage.py runserver` 

## 4. 장고 모델
1. 객체
    * 장고 안의 모델은 객체의 특별한 종류이다
    * 모델을 저장하면 그 내용이 데이터베이스에 저장된다
2. 어플리케이션 만들기
    * 잘 정돈된 상태에서 시작하기 위해 프로젝트 내부에 별도의 애플리케이션을 만든다
    * 블로그 생성: `python manage.py startapp blog`
    * 어플리케이션을 만들었으면 장고에게 알려줘야 한다
      * `mysite/settings.py` 안에서 `INSTALLED_APPS`을 열어 `'blog'`를 추가해준다
3. 블로그 글 모델 만들기
    * 모든 `Model` 객체는 `blog/models.py`에 선언하여 모델을 만든다
    * 이 파일에 우리의 블로그 글 모델을 정의한다
4. 데이터베이스에 새로운 모델을 추가
    * `python manage.py makemigrations blog`: 변동사항 확인
    * `python manage.py migrate blog`: 변동사항 적용

## 5. 장고 관리자
1. 관리자 화면 언어 설정
    * `settings.py`: `LANGUAGE_CODE = 'ko'`
2. 모델링한 글들을 장고 관리자에서 추가·수정·삭제 가능
3. `Post` 모델 등록
    * `blog/admin.py`: `admin.site.register(Post)`
4. `Post` 모델 확인
    * 슈퍼사용자 생성: `python manage.py createsuperuser`
    * 로그인: http://127.0.0.1:8000/admin/

## 6. 배포하기
1. GitHub
    1. 로컬에서 작업한 파일을 Git repository에 commit
    2. `.gitignore` 파일 생성
2. Pythonanywhere
    1. Console에서 repository 복사: `git clone https://github.com/Jiseong-Michael-Yang/my-first-blog`
    2. 파일 확인: `tree my-first-blog`
    3. 가상환경
         * 생성: `virtualenv --python=python3.7 tutorial`
         * 활성화: `source tutorial/bin/activate`
    4. 데이터베이스 생성
       * 데이터베이스 초기화: `python manage.py migrate`
    5. Web app으로 `blog` 배포
        * Pythonanywhere에 코드 복사, 가상환경·정적파일 준비, 데이터베이스 초기화
        * Pythonanywere > Web > Add a new web app
    6. 가상환경 설정
        * Pythonanywhere > Web > Virtualenv
    7. WSGI 파일 설정하기
         * WSGI 프로토콜
           * Python을 이용한 웹사이트를 서비스하기 위한 표준
           * Django는 WSGI 프로토콜을 사용해 작동
           * WSGI 설정 파일을 우리가 만든 장고 `blog`를 Pythonanywhere에서 인식하도록 수정 (Pythonanywhere > Web > Code > WSGI configuration file)

## 7. 장고 URLs
1. 첫번째 Django URL 만들기
   * `mysite/urls.py` 파일을 깨끗한 상태로 유지하기 위해 `blog` app에서 메인 `mysite/urls.py` 파일로 url을 가져옴

## 8. 장고 View 만들기
* `View`는 app의 '로직'을 넣는 곳
* `Model`에서 필요한 정보를 받아와 `Template`에 전달하는 역할
* `blog/views.py`에서 `request`를 받아와 `post_list.html` 템플릿을 호출하는 함수 정의 
* `blog/urls.py`에서는 http://127.0.0.1:8000/으로 접속했을 때 `views.post_list`를 호출하도록 정의

## 9. 장고 Template
* `blog/tempaltes/blog`에 템플릿 파일 생성(HTML)
* 변경사항 Git에 `commit` 후 Pythonanywhere에서 `pull`
* 페이지 reload 후 확인

## 10.장고 ORM과 쿼리셋(QuerySets)
* 장고를 데이터베이스에 연결하여 데이터를 저장
* 쿼리셋이란?
  * 전달받은 모델의 객체 목록
  * 쿼리셋은 데이터베이스로부터 데이터를 읽고, 필터를 걸거나 정렬할 수 있음
1. 장고 쉘(Shell)
    * `python manage.py shell`
    * `InteractiveConsole` 실행
2. 모든 객체 조회
    * `blog.models`에서 `Post` 모델 불러오기: `from blog.models import Post`
    * 게시글 목록 확인: `Post.objects.all()`
3. 객체 생성 
    * `User` 모델의 인스턴스를 가져와 `me` 변수에 전달
      * `User` 모델 불러오기: `from django.contrib.auth.models import User`
      * 사용자 확인: `User.objects.all()`
      * `me = User.objects.get(username="admin")`
    * 새 글 생성: `Post.objects.create(author=me, title='Sample title", text='Test')`
    * 글 확인: `Post.objects.all()`
3. 필터링
   * 쿼리셋의 중요한 기능은 데이터를 필터링하는 것
   * 작성자가 `me`인 모든 글 찾기: `Post.objects.filter(author=me)`
   * 제목에 'title'이라는 글자가 들어간 글 찾기: `Post.objects.filter(title__contains="title")`
   * 과거에 작성한 글 찾기: `Post.objects.filter(published_date__lte=timezone.now())`
     * `InteractiveConsole`에서 추가한 게시글은 보이지 않음
     * 게시하려는 게시물의 인스터를 얻은 후 게시
       * `post = Post.objects.get(title="Sample title")`
       * `post.publish`
       * 글 확인: `Post.objects.filter(published_date__lte=timezone.now())`
4. 정렬하기
    * 생성 날짜별 내림차순: `Post.objects.order_by('-created_date')`
    * 생성 날짜별 오름차순: `Post.objects.order_by('created_date')`
5. 쿼리셋 연결하기
      * 생성 시간대로 찾고 게시 순서대로 정렬 `Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')`
6. 종료: `exit()`

## 10. 템플릿 동적 데이터
* `blog` 글의 구조
  * `Post` 모델: `models.py`
  * `post_list` 모델: `views.py`
  * 템플릿: ??
* View는 모델과 템플릿을 연결하는 역할
    * 일반적으로 view가 템플릿에서 모델을 선택하도록 만들어야 한다
1. `blog/views.py`에서 `post_list` 뷰 내용 보기
   * 각각 다른 장소에 있는 모델을 모아주기: `from .models import Post`
   * `Post` 모델에서 블로그 글을 가져오기 위해서는 `post_list`에서 쿼리셋이 필요

## 11. 장고 템플릿
* HTML에 Python 코드를 바로 넣을 수 없기 때문에 템플릿 태그가 필요하다
* 템플릿 태그는 Python을 HTML로 바꿔주어 빠르고 쉽게 동적인 웹 사이트를 만들 수 있게 도와준다
1. Post 목록 템플릿 보여주기
    * View의 `post_list`에서 `posts`변수를 템플릿에 넘겨주었다
    * 이제 `posts` 변수를 받아 HTML에 나타나도록 해 볼 차례다
    * 장고 템플릿 안에 있는 값을 출력하려면, 변수 이름 안에 중괄호를 넣어 표시해야 한다: `{{ posts }}`
2. HTML과 템플릿 태그를 섞어 정적 블로그 게시물이 보이게 할 수 있다
3. PythonAnywhere에서 코드를 불러와도 로컬 서버에 호스팅 된 블로그에 나타나는 게시물과 일치하지 않는다
    * 로컬 컴퓨터와 PythonAnywhere의 데이터베이스는 동기화되지 않는다

## 12. CSS
1. 부트스트랩
    * HTML과 CSS 프레임워크로 미적인 웹사이트를 만들 수 있다
    * 설치: `.html` 파일 내 `<head>`에 이 링크를 넣어야 한다
      * `<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">`
      * `<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">`
2. 정적 파일
   * CSS와 이미지 파일에 해당
   * 요청내용에 따라 바뀌는 것이 아니기 때문에 모든 사용자들이 동일한 내용을 볼 수 있다
1. 정적 파일의 위치
    * 장고는 `admin` app에서 정적 파일을 어디에서 찾아야 하는지 이미 알고 있다
    * `blog` app에 `static`이라는 폴더 추가
2. CSS 파일
   * `static` 디렉토리 안에 `css`라는 새로운 디렉토리 생성
   * `css` 디렉토리 안에 `blog.css`라는 파일 생성
3. 부트스트랩을 이용하여 정적 파일 로딩
   * 제일 첫 줄에 정적 파일 로딩 선언: `{% load static %}`
   * `<head>`와 `</head>` 사이에 부트스트랩 CSS 파일 링크 추가
     * `<link rel="stylesheet" href="{% static 'css/blog.css' %}">`
   * 폰트 바꾸기
     * `<head>`와 `</head>` 사이에 `<link href="//fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext" rel="stylesheet" type="text/css">` 추가
     * `css/blog.css`에서 `h1 a` 선언블록에 `font-family: 'Lobster'` 추가하고 새로고침
   * CSS 선택자들을 활용하여 HTML 태그에 접근
  
## 13. 템플릿 확장하기
* 웹 사이트 안의 서로 다른 페이지에서 HTML의 일부를 재사용 가능
1. 기본 템플릿 생성하기
   * `blog/templates/blog/`에 `base.html` 파일 생성
   * 홈페이지 전체에 걸쳐 재사용되는 부분을 제외하고 상황에 맞는 컨텐츠가 들어갈 자리를 지정
     * `{% block content %}`
        `{% endblock %}`
    * 컨텐츠에 해당하는 HTML 파일에서는 컨텐츠에 해당하는 부분 위 아래로 블록 선언
      * `{% block content %}`
        `<!-- 컨텐츠 내용 -->`
        `{% endblock %}`
    * 두 템플릿의 연결
      * 컨텐츠가 들어가는 HTML 파일의 첫 줄에 확장 선언: `{% extends 'blog/base.html' %}`

## 14. 프로그램 애플리케이션 확장하기
1. `Post`에 템플릿 링크 만들기
    * 태그의 `href` 속성에 값 지정
      * `{% url 'post_detail' pk=post.pk %}`
      * 이 태그의 `url`은 `post_detail` 뷰를 실행시키고, 각 레코드의 고유값은 `post.pk` 로 접근한다
2. `Post` 상세 페이지 URL 만들기
    * `post_detail` 뷰가 보이게 `urls.py`에 URL 만들기
    * 첫 게시물의 상세 페이지 URL: http://127.0.0.1:8000/post/1/
    * `blog.urls`에 다음 규칙 추가
      * `path('post/<int: k>/, views.post_detail, name="post_detail")`
      * http://127.0.0.1:8000을 통한 접속에서 뒤에 post와 정수인 k로 이루어진 URL 패턴이 발견되면
      * `post_detail` 뷰로 요청을 보내 쿼리셋을 통해 게시글 상세 페이지 템플릿을 보여줄 것

## 15. 장고 폼
* 블로그 글을 추가하거나 수정하는 기능
* 폼(양식, forms)으로 강력한 인터페이스를 만들 수 있다
* 아무런 준비 없이도 양식을 만들 수 있고 `ModelForm`을 생성해 자동으로 모델에 결과물 저장 가능
1. 폼을 만들어서 `Post` 모델에 적용
   * `blog` 디렉토리 안에 `form.py` 파일 생성
       * `forms`와 `Post` import
       * `PostForm` 클래스를 생성하고 `forms.ModelForm`을 상속시킴으로서 장고에게 이 클래스가 폼이라는 것을 알려주기
       * `class Meta` 구문에 우리가 이 폼을 만들기 위해 사용할 `model`과 `fields`를 알려주기
   * URL에 연결
      * `/post/new`을 `post_new` 뷰에 보내고 이름은 `post_new`로 지정
   * View 생성
       * `post_new` 뷰를 생성
       * 미리 정의한 `PostForm` 변수 할당: `form = PostForm`
       * 매개변수 `form`을 템플릿 `post_edit.html`에 넘겨주기
   * 템플릿 생성
       * `'base.html'`에 확장
      * 폼 및 버튼 생성
2. 폼 저장하기
    * `post_new` 뷰를 불러온다
    * `method="POST"`의 의미
      * 우리가 입력했던 데이터를 `request.POST`에 저장할 것
      * 여기서 `POST`는 글을 등록하는 것을 의미
    * `post_new`의 두 가지 상황
        1. 폼에 첫 글을 작성할 때
        2. 폼에 입력된 데이터를 view 페이지로 가져올 때
            * 폼을 생성하고 `request.Post`를 넘겨주기
            * 폼의 값이 올바른 경우
              * 폼 저장
              * 사용자 저장
              * 게시일 저장
              * 변동사항 저장
3. 폼 저장 후 `post_detail` 페이지로 이동
    * `from django.shorcuts import redirect` 추가
    * `return redirect('post_detail', pk=post.pk)`
4. 폼 검증하기
* 블로그 글에는 `title`과 `text`가 반드시 있어야 한다
* `Post` 모델에서는 이 값들이 필요 없다고 했지만, 장고는 모두 기본 값으로 설정되어 있다고 간주
5. 폼 수정하기
    * `post_detail.html`에서 수정 버튼 추가
    * `post_edit` URL 추가
    * `post_edit` 뷰 추가
      * 글을 새로 쓰는 경우: 첫 번째 `if`문에서 `form = PostForm(request.POST, instance=post)`
      * 있던 글을 수정하는 경우: 첫 번째 `if`문에 대한 `else`문에서 `form = PostForm(instance=post)`
6. 보안
* 웹 사이트에는 나에게만 보이고 다른 사람에게는 보이지 않는 기능이 필요
* 글 추가, 수정 버튼에 대해서 `if`문 추가
  * `{% if.user.is_authenticated %}`
  `{% endif %}`