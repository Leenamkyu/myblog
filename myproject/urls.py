from django.contrib import admin
from django.urls import path, include
import blogapp.views
import portfolio.views
import accounts.views
from django.conf import settings#media 파일 업로드 하기 위해서 필수 추가 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blogapp.views.home, name = "home"),
    path('blog/',include('blogapp.urls')),
    path('portfolio/',portfolio.views.portfolio, name="portfolio"),
    path('accounts/', include('accounts.urls')),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
