from . import views
from django.urls import path
urlpatterns=[path('',views.MemberListView.as_view()),
             path('activity/',views.ActivityListView.as_view())]
