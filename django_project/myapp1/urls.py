from django.urls import path
from myapp1 import views

urlpatterns = [
    path('createuser/', views.create_user, name='Create_User'),
    path('createproject/', views.create_project, name='Create Project'),
    path('assignproject/', views.assign_project, name='Assign Project'),
    path('project/assignmentor/', views.assign_mentors, name='Assign Mentor'),
    path('project/mentor/<int:mentor_id>/', views.get_mentees, name='Get mentees'),
    path('user/<int:mentor_id>/projects/', views.get_projects, name='Get Projects'),
    path('project/<int:project_id>/', views.get_users, name="Get users and mentors"),
]