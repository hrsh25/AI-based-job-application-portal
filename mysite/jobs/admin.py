from django.contrib import admin
from .models import Job, Applicant, question, answer, Result

admin.site.register(Job)
admin.site.register(Applicant)
admin.site.register(question)
admin.site.register(answer)
admin.site.register(Result)