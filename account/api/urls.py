from django.urls import path
from account.api import views

urlpatterns = [
    path('accounts/', views.AccountListAPIView.as_view(), name="accounts"),
    path('account-create/', views.AccountCreateAPIView.as_view(), name="account-create"),
    path('account-update/<int:id>/', views.AccountUpdateAPIView.as_view(), name="account-update"),
    path('account-destroy/<int:id>/', views.AccountDestroyAPIView.as_view(), name='account-destroy'),
    path('students/', views.StudentListAPIView.as_view(), name="students"),
    path('student-create/', views.StudentCreateAPIView.as_view(), name='student-create'),
    path('student-update/<int:id>/', views.StudentUpdateAPIView.as_view(), name="student-update"),
    path('student-destroy/<int:id>/', views.StudentDestroyAPIView.as_view(), name="student-destroy"),
    path('teachers/', views.TeacherListAPIView.as_view(), name="teachers"),
    path('teacher-create/', views.TeacherCreateAPIView.as_view(), name="teacher-create"),
    path('teacher-update/<int:id>/', views.TeacherUpdateAPIView.as_view(), name='teacher-update'),
    path('teacher-destroy/<int:id>/', views.TeacherDestroyAPIView.as_view(), name = "teacher-destroy"),
    path('classes/', views.ClassListAPIView.as_view(), name="classes"),
    path('class-create/', views.ClassCreateAPIView.as_view(), name='class-create'),
    path('class-update/<int:id>/', views.ClassUpdateAPIView.as_view(), name="class-update"),
    path('class-destroy/<int:id>/', views.ClassDestroyAPIView.as_view(), name="class-destroy"),
    path('subjects/', views.SubjectListAPIView.as_view(), name="subjects"),
    path('subject-create/', views.SubjectCreateAPIView.as_view(), name='subject-create'),
    path('subject-update/<int:id>/', views.SubjectUpdateAPIView.as_view(), name="subject-apdate"),
    path('subject-destroy/<int:id>/', views.SubjectDestroyAPIView.as_view(), name="subject-destroy"),
    path('homeworks/', views.HomeworkListAPIView.as_view(), name="homeworks"),
    path('homework-create/', views.HomeworkCreateAPIView.as_view(), name="homework-create"),
    path('homework-update/<int:id>/', views.HomeworkUpdateAPIView.as_view(), name="homework-update"),
    path('homework-destroy/<int:id>/', views.HomeworkDestroyAPIView.as_view(),name="homewrok-destroy"),
]





