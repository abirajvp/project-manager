from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('signup', views.signup,name="signup"),
    path('signin/', views.signin,name="signin"),
    path('signout/', views.signout,name="signout"),
    path('search-users/', views.search_users, name='search_users'),
    path('get-peers', views.get_peers, name="get-peers"),
    path('get-projects', views.get_projects, name="get-projects"),
    path('get-tasks/<int:projectid>/', views.get_tasks, name="get-tasks"),
    path('update-task-status', views.update_task_status, name='update-task-status'),
    path('profile', views.profile, name='profile'),
    path('edit-profile', views.edit_profile, name='edit-profile'),
    path('assign-task', views.assign_task, name='assign-task'),
    path('view-project', views.view_project, name='view-project'),
    path('get-task-list', views.get_task_list, name='get-task-list'),
    path('get-project-tasks', views.get_project_tasks, name='get-project-tasks'),
    path('add-task-pull-request', views.add_task_pull_request, name='add-task-pull-request'),
    path('add-task-correction', views.add_task_correction, name='add-task-correction'),
    path('hold-task', views.hold_task, name='hold-task'),
    path('task-detail/', views.task_detail, name='task-detail'),
    path('sort-tasks-by-status', views.sort_tasks_by_status, name='sort-tasks-by-status'),
    path('delete-project', views.delete_project, name='delete-project'),
    path('delete-task', views.delete_task, name='delete-task'),
    path('remove-assigned-peer', views.remove_assigned_peer, name='remove-assigned-peer'),
    path('change-project-status', views.change_project_status, name='change-project-status'),
]