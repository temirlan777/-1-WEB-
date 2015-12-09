from django.conf.urls import url

from. import views

urlpatterns = [
	#url(r'^$', views.hello, name='hell#,
    #url(r'#"""params$', views.params, #name='params'),
    #url(r'^#idex$', views.index, name=#'index'),
    #url(r'^first$', views.first, name='first'),
    url(r'^$', views.NewQuestions, name='NewQuestions'),
    url(r'^signup/$', views.Signup, name='Signup'),
    url(r'^login/$', views.Login, name='Login'),
    url(r'^question/(?P<question_id>\d+)$', views.OneQuestion, name='OneQuestion'),
    url(r'^ask/$', views.Ask, name='Ask'),
    url(r'^hot/$', views.BestQuestions, name='BestQuestions'),
    url(r'^tag/(?P<tag>[A-Za-z0-9-]+)/$', views.TagsQuestions, name='TagsQuestions'),
    
 ]