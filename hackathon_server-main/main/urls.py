from django.contrib import admin
from django.urls import path
# index는 대문, blog는 게시판
from main.views import index
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # 웹사이트의 첫화면은 index 페이지이다 + URL이름은 index이다
    path('', index, name='index'),
    
]