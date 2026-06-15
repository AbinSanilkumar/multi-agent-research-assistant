from django import forms

class ResearchForm(forms.Form):
    topic = forms.CharField(
        max_length=500
    )