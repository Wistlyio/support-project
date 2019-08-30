# from django.conf.urls import url, include 
# from rest_framework.urlpatterns import format_suffix_patterns 
# from .views import StudentView, StudentDetailsView

# urlpatterns ={
#     url(r'^student/$', StudentView, name="student"),
#     url(r'^student/(?P<pk>[0-9]+)/$', StudentDetailsView, name="student_details"),
# }

# urlpatterns = format_suffix_patterns(urlpatterns)

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TicketView, TicketDetailsView
from .views import AgentView, AgentDetailsView

urlpatterns ={
    url(r'^ticket/(?P<key>.+)/$', TicketView, name = "ticket"),
    url(r'^ticket/(?P<pk>[0-9]+)/(?P<key>.+)/$', TicketDetailsView, name="ticket_details"),
    url(r'^agent/(?P<key>.+)/$', AgentView, name = "agent"),
    url(r'^agent/(?P<pk>[0-9]+)/(?P<key>.+)/$', AgentDetailsView, name="agent_details")
}

urlpatterns = format_suffix_patterns(urlpatterns)