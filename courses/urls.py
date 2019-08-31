from django.urls import path
from . import views




urlpatterns = [

    path('', views.Account.as_view(), name="account"),
    path('suggest/', views.suggestion_view, name="suggest"),
    path("course-list", views.course_list, name="course_list"),
    path("course/<int:pk>", views.course_detail, name="course-detail")



]