# Desc: URL patterns for the debug app
from django.urls import path
from . import views
urlpatterns = (
    [
     path('',views.profile.as_view()),  
     path('<int:pk>/',views.profileDetail.as_view()),
    ]
)