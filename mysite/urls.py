"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 'admin/'으로 시작하는 모든 URL을 view와 대조; 해당 URL은 무수히 많기 때문에 정규표현식 사용
    path('admin/', admin.site.urls), \
    # ; admin 이외의 URL은 `blog` 메인 app에서 가져오기
    path('', include('blog.urls')), \
]
