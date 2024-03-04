from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path("MentorLogin",views.mentorlogin,name = 'Login'),
    path("Student",views.studentlogin,name = 'studentlogin'),
    path("Adminstration",views.adminlogin,name = 'adminlogin'),
    path("Admin",views.admin,name="admin"),
    path('update_status', views.update_status, name='update_status'),
    path("Mentor",views.studentmentee,name="StudentTable"),
    path('view-absent/<str:StudentID>/', views.view_absent_records, name='view_absent_records'),
    path("Form/<str:StudentID>",views.absentpage,name ="TableForm" ),
    path("Studentpage",views.studentpage,name = "Studentpage"),
    path("ProfileMentor",views.profilementor,name = "ProfileMentor"),
    path('AbsentFormHistory', views.absent_form_history, name='AbsentFormHistory'),
    path("absent",views.absentpage,name="absent"),
    path("Form/absenttable/<str:StudentID>",views.absenttable,name="absenttable"),
    path("update/update_data/<str:StudentID>",views.updatestudent,name='updatestudent'),
    path("update/<str:StudentID>",views.update,name='update'),
    path("delete/<str:StudentID>",views.delete,name='delete'),
    path("delete/delete_data/<str:StudentID>",views.delete_data,name='delete_data'),
    path("deletestud/<str:id>",views.deletestud,name='deletestud'),
    path("delete/deletedata/<str:id>", views.deletedata, name='deletedata'),
    path("search", views.search, name='search'),

]
