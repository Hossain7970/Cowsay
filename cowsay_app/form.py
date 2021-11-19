from django import forms


class addmessageForm(forms.Form):
    text = forms.CharField(max_length=50)