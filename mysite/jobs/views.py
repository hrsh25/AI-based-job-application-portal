from django.views import generic
from django.shortcuts import render, redirect
from jobs.eval import function
from .models import Applicant, Job, question,answer, Result
from .forms import JobForm, Question_Form
from .resume import extract_text_from_pdf, extract_skills, extract_name, extract_mobile_number, extract_email, get_matching_skills
from django.urls import reverse_lazy
import os
from . import eval
import cgi
import requests
from django.core.files.storage import FileSystemStorage


class IndexView(generic.ListView):
    template_name = 'jobs/index.html'

    def get_queryset(self):
        return Job.objects.all()


class DetailView(generic.DetailView):
    model = Job
    template_name = 'jobs/details.html'


class ApplyView(generic.CreateView):
    model = Applicant
    form_class = JobForm
    template_name = 'jobs/apply.html'
    success_url = reverse_lazy('applicant_details')


# Details.get_queryset()


class Details(generic.ListView):
    template_name = 'jobs/applicant_details.html'

    def get_queryset(self):
        # exec(compile(open("jobs/resume.py").read(), 'resume.py', 'exec'))
        resume = ''

        for _ in os.listdir("C:\\Users\\harsh\\Desktop\\newsite\\mysite\\media\\jobs\\pdfs"):
            resume = _
            break;

        dir_path = 'media/jobs/pdfs/'
        path = dir_path + resume
        text = ''
        for page in extract_text_from_pdf(path):
            text += ' ' + page
        # resume =
        global name, phone, email, skills
        name = extract_name(text)
        phone = extract_mobile_number(text)
        email = extract_email(text)
        skills = extract_skills(text)
        matching_skills = get_matching_skills()
        details = Applicant(resume=path, name=name, phone=phone, email=email, matching_skills=matching_skills)
        details.save()

        for obj in Applicant.objects.all():
            if(not obj.name):
                obj.delete()

        return Applicant.objects.all()


class Questions(generic.CreateView):
    model = answer
    form_class = Question_Form
    template_name = 'jobs/questions.html'
    success_url = reverse_lazy('final')


class answerValidate(generic.ListView):
    template_name = 'jobs/final.html'
    def get_queryset(self):
        ans=[]
        for x in answer.objects.all():
            ans.append(x.answer1)
            ans.append(x.answer2)
            ans.append(x.answer3)
            ans.append(x.answer4)
            ans.append(x.answer5)

        result = function(ans)
        result = round(sum(result)/len(result), 2)

        for x in Job.objects.all():
            designation = x.Designation

        final_data = Result(Designation=designation, name=name, phone=phone, email=email, skills= skills, score = result)
        final_data.save()

        #print(ans[18:len(ans) - 3])
        #print(ans)
