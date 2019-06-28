from django.contrib import admin
from django.urls import path, include
import blogapp.views
from django.conf import settings # media
from django.conf.urls.static import static # media

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name = "home"),
    path('blog/', include('blogapp.urls')),
    path('portfolio', blogapp.views.portfolio, name='portfolio'),
    # url을 만들어준다고 무조건 html에 연결되는게 아님!
    # path('어떤 url이 들어오면', (어디에 있는)어떤 함수 실행시켜라)
] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # media

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # media