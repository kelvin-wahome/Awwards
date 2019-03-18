from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from .forms import SignupForm,ProjectForm,UpdateProfileForm,DesignForm,UsabilityForm,ContentForm
from .models import Profile,Project,UsabilityRating,DesignRating,ContentRating
from django.contrib.auth.decorators import login_required

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
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
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

@login_required(login_url='/accounts/login/')
def index(request):
  '''
  view function that renders the homepage
  '''
  form=DesignForm()
  projects = Project.get_posted_projects().order_by('-posted_on')

  return render(request,'index.html',locals())



@login_required(login_url='/accounts/login/')
def profile(request, user_id):
    '''
    Function that enables users see their profile
    '''
    form=DesignForm()
    title = "Profile"
    projects = Project.get_project_by_id(id= user_id).order_by('-posted_on')
    profiles = Profile.objects.get(user_id=user_id)
    users = User.objects.get(id=user_id)

    return render(request, 'profile/profile.html',locals())

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
