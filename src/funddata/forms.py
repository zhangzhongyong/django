from django import forms
from .models import ShowData

class ShowDataForm(forms.ModelForm):
  #tank = forms.IntegerField(widget=forms.HiddenInput(), initial=123)
  class Meta:
	model = ShowData
	fields = "__all__"

