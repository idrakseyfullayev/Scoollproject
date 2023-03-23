from rest_framework.generics import (
    ListAPIView, CreateAPIView, UpdateAPIView, RetrieveUpdateAPIView, 
    DestroyAPIView,RetrieveDestroyAPIView)
from account.api.serializers import (
    AccountListSerializer, AccountCreateSerializer, AccountUpdateSerializer,
    StudentListSerializer, StudentCreateSerializer, StudentUpdateSerializer, 
    TeacherListSerializer, TeacherCreateSerializer, TeacherUpdateSerializer,
    ClassListSerializer, ClassCreateSerializer, ClassUpdateSerializer,
    SubjectListSerializer, SubjectCeateSerializer, SubjectUpdateSerializer,
    HomeworkListSerializer, HomeworkCreateSerializer, HomeworkUpdateSerializer,
    )
from account.models import Account, Student, Teacher, Class, Subject, Homework


class AccountListAPIView(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountListSerializer

class AccountCreateAPIView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer

class AccountUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Account.objects.all()
    lookup_field = "id"
    serializer_class = AccountUpdateSerializer

class AccountDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Account.objects.all()
    lookup_field = "id"
    serializer_class = AccountListSerializer


class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer

class StudentCreateAPIView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer

class StudentUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    lookup_field = "id"
    serializer_class = StudentUpdateSerializer

class StudentDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    lookup_field = "id"
    serializer_class = StudentListSerializer        


class TeacherListAPIView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherListSerializer

class TeacherCreateAPIView(CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherCreateSerializer    

class TeacherUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Teacher.objects.all()
    lookup_field = "id"
    serializer_class = TeacherUpdateSerializer

class TeacherDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Teacher.objects.all()
    lookup_field ="id"
    serializer_class = TeacherListSerializer    



class ClassListAPIView(ListAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassListSerializer

class ClassCreateAPIView(CreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassCreateSerializer

class ClassUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Class.objects.all()
    lookup_field = "id"
    serializer_class = ClassUpdateSerializer      


class ClassDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Class.objects.all()
    lookup_field ="id"
    serializer_class = ClassListSerializer


class SubjectListAPIView(ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectListSerializer
    
class SubjectCreateAPIView(CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectCeateSerializer

class SubjectUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Subject.objects.all()
    lookup_field = "id"
    serializer_class = SubjectUpdateSerializer

class SubjectDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Subject.objects.all()
    lookup_field = "id"
    serializer_class = SubjectListSerializer


class HomeworkListAPIView(ListAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworkListSerializer

class HomeworkCreateAPIView(CreateAPIView):
    queryset = Homework.objects.all()   
    serializer_class = HomeworkCreateSerializer

class HomeworkUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Homework.objects.all()
    lookup_field = "id"
    serializer_class = HomeworkUpdateSerializer

class HomeworkDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Homework.objects.all()
    lookup_field = "id"
    serializer_class = HomeworkListSerializer


















