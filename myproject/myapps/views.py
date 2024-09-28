from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView,TemplateView
from .models import Project, Task,Contact
from .forms import ProjectForm, TaskForm,ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def send_mail_page(request):
    context = {}
    
    if request.method == 'POST':
        address = request.POST.get('address')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if address and subject and message:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                context['result'] = 'Email sent successfully'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
        else:
            context['result'] = 'All fields are required'
    
    return render(request, "myapps/index.html", context)




class ProjectListView(LoginRequiredMixin, ListView): 
    model = Project
    template_name = 'myapps/project_list.html'  
    

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm  
    #template_name = 'myapps/project_create.html'  
    success_url = "thankyou" 

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm  
    #template_name = 'myapps/project_update.html'  
    success_url = "thankyoupk"  

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'myapps/project_confirm_delete.html'  
    success_url = "thankyoupk"

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'myapps/project_detail.html'  
    


def thankyoupk(response,pk):
	return render(response, "myapps/thankyou.html", {}) 

def thankyou(response):
	return render(response, "myapps/thankyou.html", {}) 

 


class AboutUsView(TemplateView):
    template_name = 'myapps/about_us.html'

class TaskListView(ListView):
    model = Task
    template_name = 'myapps/task_list.html' 

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = "thankyou"  

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'myapps/task_form.html'
    success_url = "thankyoupk"  

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'myapps/task_confirm_delete.html'
    success_url = "thankyoupk" 

class TaskDetailView(DetailView):
    model = Task
    template_name = 'myapps/task_detail.html'  


class ContactCreate(CreateView):
 
    # specify the model for list view
    model = Contact
    form_class = ContactForm
    success_url = "thankyoupk"

def thankyoupk(response,pk):
	return render(response, "home/thankyou.html", {}) 



    
