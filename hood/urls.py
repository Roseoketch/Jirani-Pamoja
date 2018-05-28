from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^new/',views.create_profile,name='new_profile'),
    url(r'^post/',views.new_post,name='post'),
    url(r'^searched/', views.search_results, name='search_results'),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
