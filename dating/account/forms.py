from django import forms
from django.contrib.auth.models import User
from .models import Profile
from search.models import userfeature

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']



class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    # user = forms.IntegerField(widget=forms.HiddenInput, required=True)
    # returnTo = forms.CharField(widget=forms.HiddenInput, required=False, initial='/')
    class Meta:
        model = Profile
        fields = ('nickname','intro','photo','age','height','weight','gender','education','only_child','location')
class UserFeatureEditForm(forms.ModelForm):
            # user = forms.IntegerField(widget=forms.HiddenInput, required=True)
            # returnTo = forms.CharField(widget=forms.HiddenInput, required=False, initial='/')
    class Meta:
        model = userfeature
        fields = ('enjoymusic','musicloved','musichated','enjoymovie','moviehated','movieloved','hobbies')
