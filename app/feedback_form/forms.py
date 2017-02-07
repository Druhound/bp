# coding=utf-8
from django import forms

from .models import Callback, Feedback


class CallbackForm(forms.ModelForm):
    class Meta:
        model = Callback
        fields = "__all__"
        exclude = ('url',)


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"
        exclude = ('url',)


class CallbackSOUTForm2(forms.Form):
    subject = forms.CharField(max_length=50)
    email = forms.EmailField()
    name = forms.CharField(max_length=50)
    telephone = forms.CharField(max_length=20)
    message = forms.CharField(widget=forms.Textarea)
    attach = forms.Field(widget=forms.FileInput)


class EmailForm(forms.Form):
    # name = forms.CharField(required=False)
    # telephone = forms.CharField(max_length=30)
    # rab = forms.CharField(max_length=10, required=False)
    attach = forms.Field(widget=forms.FileInput, required=False)
    validation = forms.BooleanField(required=False)