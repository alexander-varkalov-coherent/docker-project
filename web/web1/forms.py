from django import forms


class CommentForm(forms.Form):
    firstname = forms.CharField(max_length=255)
    lastname = forms.CharField(max_length=255)
    age = forms.IntegerField()
    text = forms.CharField(max_length=255)
