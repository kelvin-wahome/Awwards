from django.shortcuts import render
from .models import Profile,Project
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def index(request):
  '''
  view function that renders the homepage
  '''
  form=DesignForm()
  projects = Project.get_posted_projects().order_by('-posted_on')

  return render(request,'index.html',locals())
