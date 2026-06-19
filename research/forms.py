from django import forms


class ResearchForm(forms.Form):

    topic = forms.CharField(
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter a research topic'
            }
        )
    )
