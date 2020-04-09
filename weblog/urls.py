from . import views
from django.conf import settings
from django.urls import path, include
from .views import PostList
from .feeds import LatestPostsFeed
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns


urlpatterns = [
	path('', views.PostList.as_view(), name='home'),
	path('<slug:slug>/', views.post_detail, name='post_detail'),
	path("feed/rss", LatestPostsFeed(), name="post_feed"),
	path("freelancing.html/", views.freelancing, name="freelancing"),
	path('summernote/', include('django_summernote.urls'))
	# path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]



urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)