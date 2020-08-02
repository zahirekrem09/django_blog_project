from allauth.account.forms import SignupForm
from django import forms
from blog.models.user import User
from tempus_dominus.widgets import DatePicker
from blog.choices import GenderChoices


class CustomSignupForm(SignupForm):
  first_name = forms.CharField(max_length=25, widget=forms.TextInput(
      attrs={'placeholder': 'First Name'}))
  last_name = forms.CharField(max_length=25, widget=forms.TextInput(
      attrs={'placeholder': 'Last Name'}))


class CustomUserForm(forms.ModelForm):
  birthday = forms.DateField(
      widget=DatePicker(
          options={
              'viewMode': 'years',

              'useCurrent': True,
              'collapse': False,
          },
          attrs={
              'append': 'fa fa-calendar',
              'icon_toggle': True,
          }
      ), required=False,
  )
  gender = forms.ChoiceField(choices=GenderChoices.CHOICES, widget=forms.RadioSelect,
                             required=False)

  class Meta:
    model = User
    #fields = "__all__"
    fields = ('username', 'first_name',
              'last_name', 'email', 'birthday',
              'phone_number', 'interests',
              'gender', 'marital_status',
              'educational_status', 'profession', 'profile_image'
              )
    widgets = {
        'interests': forms.CheckboxSelectMultiple,
    }


# profil foto uptade için ama olmadı
class UserProfileUpdateForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('profile_image',)
