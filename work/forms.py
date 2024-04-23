from django import forms
from work.models import User,Taskmodel



class Register(forms.ModelForm):

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':"username"}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':"enter first_name"}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':"enter last_name"}),
            'email':forms.EmailInput(attrs={'class':'form-control',}),
            'password':forms.PasswordInput(attrs={'class':'form-control',}),
        }


class Taskform(forms.ModelForm):

    class Meta:
        model=Taskmodel
        fields=['task_name','task_description']
        widgets={
            'task_name':forms.TextInput(attrs={'class':'form-control','placeholder':"enter task name"}),
            'task_description':forms.Textarea(attrs={'class':'form-control','column':20,'rows':5,'placeholder':"enter task description"})
        }

class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField()