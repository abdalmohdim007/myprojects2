from django.contrib import admin
from .models import Project, Task, Contact, Function, App, Template
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
  list_display = ('name', 'description', 'user', 'notes')

class TaskAdmin(admin.ModelAdmin):
  list_display = ('name', 'assigned_to', 'status')  

class ContactAdmin(admin.ModelAdmin):
  list_display = ("name", "email")  

class TemplateAdmin(admin.ModelAdmin):
  list_display = ('name', 'project_name')  




admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Function)
admin.site.register(Template,TemplateAdmin)
admin.site.register(App)




