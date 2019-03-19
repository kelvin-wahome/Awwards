from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$',views.index,name = 'index'),
    # url(r'^signup/$', views.signup, name='signup'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^project/$', views.upload_project, name='upload_project'),
    url(r'^user/(\d+)$', views.profile, name='profile'),
    url(r'^profile/update/$', views.update_profile, name='update_profile'),
    # url(r'^api/projects/$', views.ProjectList.as_view()),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
