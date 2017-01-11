from django import forms

from .models import OrderService, CallbackSOUT, Callback, CallbackExperts


class OrderServiceForm(forms.ModelForm):
    class Meta:
        model = OrderService
        fields = ("name", "email", "telephone", "text")


class CallbackSOUTForm(forms.ModelForm):
    class Meta:
        model = CallbackSOUT
        fields = ("name", "telephone")


class CallbackForm(forms.ModelForm):
    class Meta:
        model = Callback
        fields = ("name", "telephone", "text")


class CallbackExpertsForm(forms.ModelForm):
    class Meta:
        model = CallbackExperts
        fields = ("name", "telephone")