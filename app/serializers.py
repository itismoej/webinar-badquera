from rest_framework import serializers

from app.models import College, Lesson, Chapter


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('__all__',)


class ChapterSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Chapter
        fields = ('__all__',)


class CollegeSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True)

    class Meta:
        model = College
        fields = ('__all__',)
