from django.urls import path
from django.conf.urls import url
from . import views




urlpatterns = [

    path('', views.Account.as_view(), name="account"),
    path('suggest/', views.suggestion_view, name="suggest"),
    path("course-list", views.course_list, name="course_list"),
    path("course/<int:pk>/", views.course_detail, name="course-detail"),
    #url(r'(?P<pk>\d+)/$', views.course_detail, name='course-detail'),
    #path("text-detail/<int:pk>", views.text_detail, name="text-detail"),
    #path("quiz-detail/<int:pk>", views.quiz_detail, name="quiz-detail"),
    url(r'(?P<course_pk>\d+)/create_quiz/$', views.quiz_create,
        name='create_quiz'),

    url(r'(?P<course_pk>\d+)/t(?P<step_pk>\d+)/$', views.text_detail,
        name='text-detail'),
    url(r'(?P<course_pk>\d+)/q(?P<step_pk>\d+)/$', views.quiz_detail,
        name='quiz-detail'),

]