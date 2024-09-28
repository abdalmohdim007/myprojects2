from .models import Project, Task, Contact
from django import forms

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'apps', 'functions', 'templates', 'user', 'notes']

    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if isinstance(field, forms.ModelMultipleChoiceField):
                field.widget.attrs['multiple'] = 'multiple'


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
       
        fields = ['name', 'assigned_to', 'status']

    
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
    

        fields = ['name', 'email', 'message',]
    
   # This formats the fields, but make sure you add the template tags
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

