from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('Admin',views.admin_login_view,name='Admin'),
    path('Register',views.Register_view,name='register'),
    path('courses',views.user_dash,name='dashboard'),
    path('add-course',views.add_course,name='addcourse'),
    path('enroll/<int:pk>',views.enroll_course,name='enroll'),
    path('enroled-list',views.enrolled_course,name='enrolled'),
    path('course-view',views.course_View,name='viewcourse'),
    path('delete-course/<int:pk>/',views.course_delete,name='deletecourse'),
    path('manage-user',views.manage_user,name='manageuser'),
]
