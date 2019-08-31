from django import forms
from django.core import validators


def must_be_empty(value):
    if value:
        raise forms.ValidationError("is not empty")




class SuggestionForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Please verify your email address")  #or use help_text
    suggestion = forms.CharField(widget=forms.Textarea)
    juicy = forms.CharField(required=False,
                            widget=forms.HiddenInput,
                            label="leave empty",
                            validators=[must_be_empty])


    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data['email']
        verify = cleaned_data['verify_email']

        if email !=verify:
            raise forms.ValidationError("You need to enter the same email in both fields")
