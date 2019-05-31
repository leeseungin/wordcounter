"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
import wordcounter.views
#wordcounter에 있는 views에 있는 것을 가져온다는 명령어, 파일이 여러개인 경우 다음과 같이 지정을 해주는 것이 좋다. 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wordcounter.views.home, name="home"),
    #초기 화면의 경우 home으로 설정하면 기타 경로는 필요없다.     
    path('/about', wordcounter.views.about, name="about"),
    path('/count', wordcounter.views.count, name="count"),
    #초기 화면이 아닌 경우에는 따로 경로를 설정해 줄 필요가 있다. 
    #name은 어떤 페이지로 보낼 때 사용하는 이름에 해당. 
    path('select/', wordcounter.views.select, name='select'),
    #3번째 select라는 이름으로 html파일에서 정보가 왔을때, 1번째 url은 127.0.0.1/select로 보내고
    #2번째 views.py에 있는 select 함수를 실행시킨다. 
    # path('blog/create', blog.views.create, name='create'),
    
]
