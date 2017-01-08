from django.conf.urls import patterns, url
from compilador import views

urlpatterns = patterns('compilador.views',	
	url(r'^$', 'index_view', name='index')
  
    )


#    """
#    # ex: /polls/5/results/
#    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
#    # ex: /polls/5/vote/
#    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
#    """
#)
