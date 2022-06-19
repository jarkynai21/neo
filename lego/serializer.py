from rest_framework import serializers
from .models import Course,Category,Contact,Branch



class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'category', 'logo', 'contact']


    def create(self, validated_data):
        categories_data = validated_data.pop("category")
        course_data = validated_data.pop("course")
        course = Course.objects.create(**validated_data)

        for category_data in categories_data:
            Category.objects.create(course=course, **category_data)
        for course_data in course_data:
            Course.objects.create(course=course, **course_data)

        return course


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name','category','image','created']