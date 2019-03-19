from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .forms import SignupForm, ProjectForm, UpdateProfileForm, DesignForm, UsabilityForm, ContentForm
# from .serializer import ProjectSerializer,ProfileSerializer
from .models import Profile, Project, UsabilityRating, DesignRating, ContentRating
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your Awwwards account.'
            message = render_to_string('registration/activate_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.''<a href="/accounts/login/"> click here </a>')
    else:
        return HttpResponse('Activation link is invalid!')

@login_required(login_url='/accounts/login/')
def index(request):
    '''
    view function that renders the homepage
    '''
    form = DesignForm()
    projects = Project.get_posted_projects().order_by('-posted_on')

    return render(request, 'index.html', locals())

@login_required(login_url='/accounts/login/')
def search_results(request):
  if 'project' in request.GET and request.GET["project"]:
    form=DesignForm()
    title = request.GET.get("project")
    searched_projects = Project.search_project(title)
    message = f"{title}"

    return render(request, 'search.html',{"message":message,"projects":searched_projects,"form":form})

  else:
    message = "You haven't searched for anything"
    return render(request, 'search.html',{"message":message})

@login_required(login_url='accounts/login/')
def upload_project(request):
    profile = Profile.objects.all()
    for profile in profile:
      if request.method == 'POST':
          form = ProjectForm(request.POST, request.FILES)
          if form.is_valid():
              add=form.save(commit=False)
              add.profile = profile
              add.user = request.user
              add.save()
              return redirect('index')
      else:
          form = ProjectForm()


      return render(request,'upload.html',locals())

@login_required(login_url='/accounts/login/')
def profile(request, user_id):
    '''
    Function that enables users see their profile
    '''
    form = DesignForm()
    title = "Profile"
    projects = Project.get_project_by_id(id=user_id).order_by('-posted_on')
    profiles = Profile.objects.get(user_id=user_id)
    users = User.objects.get(id=user_id)

    return render(request, 'profile/profile.html', locals())


@login_required(login_url='/accounts/login/')
def update_profile(request):
    '''
    Function that enables one to update their profile details
    '''
    current_user = request.user
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('index')
    else:
        form = UpdateProfileForm()
    return render(request, 'profile/update_profile.html', locals())

@login_required(login_url='/login')
def rate_usability(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = UsabilityForm(request.POST)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.project = project
            vote.user_name = request.user
            vote.profile = request.user.profile

            vote.save()
        return redirect('index')

    return render(request, 'index.html')

@login_required(login_url='/login')
def rate_design(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = DesignForm(request.POST)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.project = project
            vote.user_name = request.user
            vote.profile = request.user.profile

            vote.save()
        return redirect('index')
    else:
        form = DesignForm()

    return render(request, 'index.html',locals())


@login_required(login_url='/login')
def rate_content(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.project = project
            vote.user_name = request.user
            vote.profile = request.user.profile

            vote.save()
        return redirect('index')

    return render(request, 'index.html')
