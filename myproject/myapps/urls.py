from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [ 
path('', login_required(views.ProjectListView.as_view()), name='project-list'),
path('project/', views.ProjectListView.as_view(), name='project'),
path('project/create/', views.ProjectCreateView.as_view(), name='project_create'),
path('project/<int:pk>/update/', views.ProjectUpdateView.as_view(), name='projrct_update'),
path('project/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'),
path('project/<int:pk>/detail/', views.ProjectDetailView.as_view(), name='project_detail'),
path('project/<pk>/delete/thankyoupk', views.thankyoupk, name='thankyoudeletepk'),
path('project/<pk>/update/thankyoupk', views.thankyoupk, name='thankyoupk'),
path('project/create/thankyou', views.thankyou, name='thankyou'),
##########################################################################################
path('task', views.TaskListView.as_view(), name='task'),
path('task/create/', views.TaskCreateView.as_view(), name='task_create'),
path('task/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task_update'),
path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
path('task/<int:pk>/detail/', views.TaskDetailView.as_view(), name='task_detail'),
path('task/<pk>/delete/thankyoupk', views.thankyoupk, name='thankyoudeletepk'),
path('task/<pk>/update/thankyoupk', views.thankyoupk, name='thankyoupk'),
##########################################################################################
 path('contact', views.ContactCreate.as_view(),name='contact'),
path('aboutuss', views.AboutUsView.as_view(), name='about_us'),
] 