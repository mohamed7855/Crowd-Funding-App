from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'details', 'category', 'tags', 'totalTarget', 'images']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Project Title'}),
            'details': forms.Textarea(attrs={'placeholder': 'Project Detail'}),
            # 'category': forms.Select(attrs={'placeholder': 'Project Category'}),
            'tags': forms.TextInput(attrs={'placeholder': 'Tags'}),
            'totalTarget': forms.NumberInput(attrs={'placeholder': 'Total Target'}),
            # 'startTime': forms.DateTimeInput(attrs={'placeholder': 'Start Date'}),
            # 'endTime': forms.DateTimeInput(attrs={'placeholder': 'End Date'}),
            'images': forms.FileInput(attrs={'placeholder': 'Choose Image'}),
            'category': forms.Select(attrs={'class': 'select-placeholder'}),

        }
