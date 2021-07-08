from django.contrib import admin
from django.urls import path

from app.views import CollegeView, AllCollegesView, LessonView, AllLessonsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lessons/<int:lesson_id>/', LessonView.as_view()),
    path('lessons/all/', AllLessonsView.as_view()),
    path('colleges/<int:college_id>/', CollegeView.as_view()),
    path('colleges/all/', AllCollegesView.as_view()),
]
