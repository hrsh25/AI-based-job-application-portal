from django import forms

from .models import Applicant,question,answer

class JobForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = {'resume'}

class Question_Form(forms.ModelForm):
    class Meta:
        model = answer
        fields = {'answer1', 'answer2', 'answer3', 'answer4', 'answer5'}
