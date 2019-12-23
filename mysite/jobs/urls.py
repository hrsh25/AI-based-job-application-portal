from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),
    url(r'^(?P<pk>[0-9]+)/jobs/apply.html', views.ApplyView.as_view(), name='apply'),
    url(r'jobs/apply/applicant_details.html', views.Details.as_view(), name='applicant_details'),
    #url(r'jobs/apply/applicant_details/questions.html+$', views.getdetails, name='getdetails'),
    url(r'jobs/apply/applicant_details/questions.html+$', views.Questions.as_view(), name='questions'),
    #url(r'jobs/apply/applicant_details/questions.html', views.getQuestions.as_view(), name='questions'),
    url(r'jobs/apply/applicant_details/questions/final.html+$', views.answerValidate.as_view(), name='final'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

