from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register('course',CourseView)
router.register('category',CategoryView)


urlpatterns = [
    path('course/',views.as_view()),
    path('category/',views.as_view()),
    path('course/<int:course_id>/',CourseView.as_view),
    path('', include(router.urls)),

]