# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth import authenticate, login
from .forms import LoginForm,UserRegistrationForm,UserEditForm, ProfileEditForm,UserFeatureEditForm
from .models import Profile
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.views.generic import DeleteView, TemplateView
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from search.models import userfeature,hobbies,movie,music
from dating.helper import getgender,geteducation,getlocation,getonlychild

# DEFAULT_RETURNTO_PATH = getattr(settings, 'DEFAULT_RETURNTO_PATH', '/')



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html',  {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            profile = Profile.objects.create(user=new_user)
            return render(request,
                         'account/register_done.html',
                         {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                 'account/register.html',
                 {'user_form': user_form})

def viewprofile(request,pk=None):
    if pk :
        profile = Profile.objects.get(pk=pk)

    else:
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)

    username = profile.user.username
    user = profile.user
    G = getgender(profile.gender)
    EDU = geteducation(profile.education)
    L= getlocation(profile.location)
    OC = getonlychild(profile.only_child)
    if profile.user.id % 10 != 0:
        if profile.gender == "M":
            l4 = "Woman"
        else:
            l4 = "Man"
    else:
        if profile.gender == "M":
            l4 = "Man"
        else:
            l4 = "Woman"

    if profile.intro == "":
        if profile.gender == "M":
            intro = "He haven't write anything yet. ╥﹏╥"
        elif profile.gender == "F":
            intro = "She haven't write anything yet. ╥﹏╥"
        else:
            intro = "He/She haven't write anything yet. ╥﹏╥"
    else:
        intro = profile.intro

    ufeature = userfeature.objects.get(user = request.user)
    lmusic = ufeature.musicloved.all()
    hmusic = ufeature.musichated.all()
    lmovie = ufeature.movieloved.all()
    hmovie = ufeature.moviehated.all()
    hobbies = ufeature.hobbies.all()





    data = {'profile':profile,'pk':pk,'username':username,'G':G,'EDU':EDU,"L":L,"onlychild":OC,"l4":l4,"intro":intro}

    data["ufeature"] = ufeature
    data["lmusic"] = lmusic
    data["hmusic"] =hmusic
    data["lmovie"] = lmovie
    data["hobbies"] = hobbies


    # user_feature = userfeature.objects.get(user=profile.user)
    return render(request,'account/profile.html', data)




def viewprofilewithname(request,username=None):
    if username:
        user = User.objects.get(username=username)
        # user_feature = userfeature.objects.get(user=user)
        profile = Profile.objects.get(user=user)

    else:
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            # user_feature = userfeature.objects.get(user=request.user)

    pk = profile.pk

    G = getgender(profile.gender)
    EDU = geteducation(profile.education)
    L= getlocation(profile.location)
    OC = getonlychild(profile.only_child)
    if profile.user.id % 10 != 0:
        if profile.gender == "M":
            l4 = "Woman"
        else:
            l4 = "Man"
    else:
        if profile.gender == "M":
            l4 = "Man"
        else:
            l4 = "Woman"

    if profile.intro == "":
        if profile.gender == "M":
            intro = "He haven't write anything yet. ╥﹏╥"
        elif profile.gender == "F":
            intro = "She haven't write anything yet. ╥﹏╥"
        else:
            intro = "He/She haven't write anything yet. ╥﹏╥"
    else:
        intro = profile.intro

    ufeature = userfeature.objects.get(user = request.user)
    lmusic = ufeature.musicloved.all()
    hmusic = ufeature.musichated.all()
    lmovie = ufeature.movieloved.all()
    hmovie = ufeature.moviehated.all()
    hobbies = ufeature.hobbies.all()





    data = {'profile':profile,'pk':pk,'username':username,'G':G,'EDU':EDU,"L":L,"onlychild":OC,"l4":l4,"intro":intro}

    data["ufeature"] = ufeature
    data["lmusic"] = lmusic
    data["hmusic"] =hmusic
    data["lmovie"] = lmovie
    data["hobbies"] = hobbies

    return render(request,'account/profile.html', data)
# def viewprofile(request,username=None):
#     ctx = {'username':username}
#     if request.method == 'POST':
#         if username:
#             profile = Profile.objects.get(username=username)
#         else:
#             if request.user.is_authenticated:
#                 profile = Profile.objects.get(user=request.user)
#
#     return render(request,'account/profile.html', {'profile':profile},ctx)


@login_required
def edit(request):

    profile = Profile.objects.get(user=request.user)
    user_feature = userfeature.objects.get(user=request.user)
    lmusic = user_feature.musicloved.all()
    hmusic = user_feature.musichated.all()
    lmovie = user_feature.movieloved.all()
    hmovie = user_feature.moviehated.all()
    lhobbies = user_feature.hobbies.all()


    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                data=request.POST)
        profile_form = ProfileEditForm(instance = profile,
                                        data=request.POST,
                                        files=request.FILES)

        userfeature_form =UserFeatureEditForm(instance = user_feature,
                                              data=request.POST,
                                              files=request.FILES)
        if user_form.is_valid():
            user_form.save()
        else:
            messages.error(request, 'Error updating your profile')

        if profile_form.is_valid():
            profile_form.save()
        else:
            messages.error(request, 'Error updating your profile')

        if userfeature_form.is_valid():
            userfeature_form.save()
        else:
            messages.error(request, 'Error updating your profile')


            messages.success(request, 'Profile updated '\
                                     'successfully')

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=profile)
        userfeature_form =UserFeatureEditForm(instance = user_feature)

    data = {'user_form': user_form,'profile_form': profile_form,'userfeature_form':userfeature_form,'profile':profile,"ufeature":user_feature}

    data["lmusic"] = lmusic
    data["hmusic"] =hmusic
    data["lmovie"] = lmovie
    data["lhobbies"] = lhobbies

    data["music"] = music.objects.all()
    data["movie"] = movie.objects.all()
    data["hobbies"] = hobbies.objects.all()

    return render(request,
                 'account/edit.html',
                 data)

def index(request):
    data ={}
    data['profile']= Profile.objects.all().reverse()[:10]
    return render(request, 'index-2.html',data)
