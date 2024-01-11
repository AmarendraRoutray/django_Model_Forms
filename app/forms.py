from django import forms
from .models import *


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'
        
        
        
class WebpageForm(forms.ModelForm):
    class Meta:
        model = Webpage
        fields = '__all__'
        
        # fields = ['name','email']
        # exclude = ['url']
        
        labels = {'topic_name':'TOPIC-NAME'}
        # widgets = {'topic_name':forms.CheckboxSelectMultiple(),'name':forms.Textarea()}
        
        
        
class AccessRecordForm(forms.ModelForm):
    class Meta:
        model = AccessRecord
        fields = '__all__'