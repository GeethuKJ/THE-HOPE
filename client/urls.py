from django.contrib import admin
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.user_dashboard, name="user_dashboard"),
    path('profile', views.user_profile, name="profile"),
    path('edit-profile-user', views.edit_profile_user, name="edit_profile_user"),
    path('solutions/', views.user_solution, name="user_solution"),
    path('create-problem/', views.post_problem, name="create_problem"),
    path('therapist/', views.user_therapist, name="user_therapist"),
    path('therapist/profile/', views.user_therapist_single, name='user_therapist_single'),
    re_path('^therapist/profile/(?P<therapist_id>.*)/$', views.user_therapist_single, name='user_therapist_single'),
]
