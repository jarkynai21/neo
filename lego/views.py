from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializer import CourseSerializer, Course
from rest_framework import views,viewsets
from rest_framework.response import Response





class CourseView(views.APIView):

    def get(self,request,*args,**kwargs):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses,many=True)
        return Response(serializer.data)


    def post(self,request,*args,**kwargs):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class CategoryView(views.APIView):

    def get(self,request,*args,**kwargs):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses)
        return Response(serializer.data)

    def delete(self,request,course_id):
        course = Course.objects.get(id=course_id)
        course.delelte()
        return Response({'date':'successfully deleted!'})