from django import forms
from django.forms.forms import Form
from django.forms.widgets import PasswordInput
#inheriting a property  from froms module in which we having a class name "Form"

# Screen 1: Login Form
# 1.Email (Input)
# 2.Password (Input)
# 3.Login Button
# 4.SignUp Link

class Login(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

# Screen 2: Sign Up Form
# 1.Username
# 2.Email
# 3.Password
# 4.Confirm Password
# 5.Address


class Signup(forms.Form):
    username = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)
    Confirm_password = forms.CharField(widget=forms.PasswordInput)
    address = forms.CharField(max_length=1000)

#now we need to passs the form in view.py function then we pass that function into templates..
#print(dir(forms))
 
