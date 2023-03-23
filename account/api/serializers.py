from rest_framework import serializers
from account.models import Account, Teacher, Student, Class, Homework, Subject

class AccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = ("password",)

class AccountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("id", "username", "password")

class AccountUpdateSerializer(serializers.ModelSerializer):                
    class Meta:
        model = Account
        fields = ('username', "first_name", 'last_name', "gender", "password")


class TeacherListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        exclude = ("password",)   

class TeacherCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ("id", "username", 'first_name', "last_name", "password")

class TeacherUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ("username", 'first_name', 'last_name', "gender", "password")


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ("password",)

class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("id", 'username', 'first_name', "last_name", "password")

class StudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('username', 'first_name', 'last_name', "gender", "password")


class ClassListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ("id", 'name', "teachers", "students", "subjects", "class_homeworks")

class ClassCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ("name",)

class ClassUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ('name',)        


class SubjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('name', "subject_class", "subject_homeworks")  # bele yazilis duzdu

class SubjectCeateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"     

class SubjectUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class HomeworkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = "__all__"
        
class HomeworkCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = "__all__"


class HomeworkUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = "__all__"        



    