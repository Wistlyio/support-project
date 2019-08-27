from django.conf.urls import url, include 
from rest_framework.urlpatterns import format_suffix_patterns 
from .views import StudentView, StudentDetailsView

urlpatterns ={
    url(r'^student/$', StudentView, name="student"),
    url(r'^student/(?P<pk>[0-9]+)/$', StudentDetailsView, name="student_details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)