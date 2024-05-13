from django.urls import path
from . import views

urlpatterns = [
    path('', views.therapist_dashboard, name="therapist_dashboard"),
    path('therapist-profile/', views.therapist_profile, name='therapist_profile'),
    path('edit-profile-therapist/', views.edit_profile_therapist, name='edit_profile_therapist'),
    path('problems/', views.problems, name="problems"),
    path('problems/<int:problem_id>/', views.view_problem, name="view_problem"),
    path('problems/delete-solution/<int:solution_id>/', views.delete_solution, name="delete_solution"),
    path('problems/<int:problem_id>/create-solution', views.post_solution, name="create_solution"),
]
