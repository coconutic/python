from django import forms

class UserSignInForm(forms.Form):
    username = forms.CharField(max_length = 30, required = True, widget = forms.TextInput(attrs = {'style' : 'margin-left: 30px;'}))
    firstname = forms.CharField(max_length = 30, required = False)
    lastname = forms.CharField(max_length = 30, required = False)
    email = forms.CharField(max_length = 30, required = True)
    password = forms.CharField(widget = forms.PasswordInput, label = "Password", \
                                min_length = 6, max_length = 30, required = True)
    confirmation = forms.CharField( widget = forms.PasswordInput, label = "Confirm Password", \
                                min_length = 6, max_length = 30, required = True)

class UserLogInForm(forms.Form):
    email = forms.CharField(max_length = 30, required = True, widget = forms.TextInput(attrs = {'style' : 'margin-left: 30px;'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'style' : 'margin-left: 30px;'}), label = "Password", \
                                min_length = 6, max_length = 30, required = True)
