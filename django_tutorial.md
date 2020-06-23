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