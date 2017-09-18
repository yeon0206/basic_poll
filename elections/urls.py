from django.conf.urls import url, include
from . import views

'''
urlpatterns = [
    url(r'^$', views.index),
    url(r'^areas/(?P<area>.+)/$', views.areas), #area매개변수 전달 .+는 아무거나다
    # url(r'^areas/(?P<area>\d+)/$', views.areas), \d는 숫자만
    url(r'^areas/(?P<area>.+)/results$', views.results),
    url(r'^polls/(?P<poll_id>\d+)/$', views.polls),
]
'''

urlpatterns = [
    url(r'^$', views.index),
    url(r'^areas/(?P<area>[가-힣]+)/$', views.areas),
    url(r'^areas/(?P<area>[가-힣]+)/results$', views.results),
    url(r'^polls/(?P<poll_id>\d+)/$', views.polls),
]
