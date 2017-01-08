from django.conf.urls import patterns, url
from compilador import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'compilador/$', views.index, name='index2')
    )


#    """
#    # ex: /polls/5/results/
#    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
#    # ex: /polls/5/vote/
#    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
#    """
#)
