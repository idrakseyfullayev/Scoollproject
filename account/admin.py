from django.contrib import admin
from account.models import Account, Student, Teacher, Class, Homework, Subject

# Register your models here.


admin.site.register(Account)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(Homework)
admin.site.register(Subject)