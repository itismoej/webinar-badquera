from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import College, Lesson
from app.serializers import CollegeSerializer, LessonSerializer


class LessonView(APIView):

    def get(self, request, lesson_id, *args, **kwargs):
        try:
            lesson = Lesson.objects.get(id=lesson_id)
            serialized_lesson = LessonSerializer(instance=lesson)
            return Response(serialized_lesson.data, status=200)
        except Lesson.DoesNotExist:
            return Response(status=404)

    def put(self, request, lesson_id, *args, **kwargs):
        if request.user.is_superuser:
            try:
                lesson = Lesson.objects.get(id=lesson_id)
                serialized_lesson = CollegeSerializer(instance=lesson, data=request.data)
                if serialized_lesson.is_valid():
                    serialized_lesson.save()
                    return Response(serialized_lesson.data, status=200)
                return Response(serialized_lesson.errors, status=400)
            except Lesson.DoesNotExist:
                return Response(status=404)

        return Response(status=403)


class AllLessonsView(APIView):

    def get(self, request, *args, **kwargs):
        lessons = Lesson.objects.all()
        serialized_lessons = LessonSerializer(instance=lessons, many=True)
        return Response(serialized_lessons.data)

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            serialized_lessons = LessonSerializer(data=request.data)
            if serialized_lessons.is_valid():
                serialized_lessons.save()
                return Response(serialized_lessons.data, status=201)
            return Response(serialized_lessons.errors, status=400)

        return Response(status=403)


class CollegeView(APIView):

    def get(self, request, college_id, *args, **kwargs):
        try:
            college = College.objects.get(id=college_id)
            serialized_college = CollegeSerializer(instance=college)
            return Response(serialized_college.data, status=200)
        except College.DoesNotExist:
            return Response(status=404)

    def put(self, request, college_id, *args, **kwargs):
        if request.user.is_superuser:
            try:
                college = College.objects.get(id=college_id)
                serialized_college = CollegeSerializer(instance=college, data=request.data)
                if serialized_college.is_valid():
                    serialized_college.save()
                    return Response(serialized_college.data, status=200)
                return Response(serialized_college.errors, status=400)
            except College.DoesNotExist:
                return Response(status=404)

        return Response(status=403)


class AllCollegesView(APIView):

    def get(self, request, *args, **kwargs):
        colleges = College.objects.all()
        serialized_colleges = CollegeSerializer(instance=colleges, many=True)
        return Response(serialized_colleges.data)

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            serialized_college = CollegeSerializer(data=request.data)
            if serialized_college.is_valid():
                serialized_college.save()
                return Response(serialized_college.data, status=201)
            return Response(serialized_college.errors, status=400)

        return Response(status=403)
