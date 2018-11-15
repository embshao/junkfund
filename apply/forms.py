from django import forms
from .models import Candidate


class ApplicationForm(forms.ModelForm):
    name = forms.CharField(label='', min_length=1, max_length=60, 
                widget=forms.TextInput(attrs={'placeholder': 'Enter first name and surname'}))
    project_name = forms.CharField(label='', min_length=1, max_length=60,
                widget=forms.TextInput(attrs={'placeholder': 'Enter Business/Project Name'}))
    project_objective = forms.CharField(label='', min_length=1, max_length=60, 
                widget=forms.Textarea(attrs={'placeholder': 'What is the objective of your business or project?'}))
    target_audience = forms.CharField(label='', min_length=1, max_length=60, 
                widget=forms.Textarea(attrs={'placeholder': 'Who is your target audience?'}))
    revenue_model = forms.CharField(label='', min_length=1, max_length=60, 
                widget=forms.Textarea(attrs={'placeholder': 'What is your revenue model? (If you do not have one, please note this too.)'}))
    project_age = forms.CharField(label='', min_length=1, max_length=60, 
                widget=forms.TextInput(attrs={'placeholder': 'How long has your business or project been operating?'}))
    contact_details = forms.CharField(label='', min_length=1, max_length=60, 
                widget=forms.Textarea(attrs={'placeholder': 'Please provide us with your business or project contact details.'}))
    class Meta:
        model = Candidate
        fields = (
            'name',
            'project_name',
            'project_objective',
            'target_audience',
            'revenue_model',
            'project_age',
            'contact_details'
        )

