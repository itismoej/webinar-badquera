from django.contrib import admin

from .models import College, Lesson


class CollegeAdmin(admin.ModelAdmin):
    pass


class LessonAdmin(admin.ModelAdmin):
    pass


admin.site.register(College, CollegeAdmin)
admin.site.register(Lesson, LessonAdmin)
