from django.contrib import admin

from .models import College, Chapter, Lesson


class CollegeAdmin(admin.ModelAdmin):
    pass


class ChapterAdmin(admin.ModelAdmin):
    pass


class LessonAdmin(admin.ModelAdmin):
    pass


admin.site.register(College, CollegeAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Lesson, LessonAdmin)
