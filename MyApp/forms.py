from django import forms


class UserForm(forms.Form):

    fname = forms.CharField(label="Имя")
    lname = forms.CharField(label="Фамилия")
