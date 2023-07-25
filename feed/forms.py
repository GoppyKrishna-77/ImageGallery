from django import forms

class PostForm(forms.Form):
    image = forms.forms.FileField()
    text = forms.CharField(label="Title")
