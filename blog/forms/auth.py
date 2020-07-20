from allauth.account.forms import SignupForm
from django import forms
from blog.models.user import User


class CustomSignupForm(SignupForm):
  first_name = forms.CharField(max_length=25, widget=forms.TextInput(
      attrs={'placeholder': 'First Name'}))
  last_name = forms.CharField(max_length=25, widget=forms.TextInput(
      attrs={'placeholder': 'Last Name'}))


class CustomUserForm(forms.ModelForm):
  class Meta:
    model = User
    #fields = "__all__"
    fields = ('username', 'first_name',
              'last_name', 'email',
              'phone_number', 'interests',
              'gender', 'marital_status',
              'educational_status', 'profession'
              )
