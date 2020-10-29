from django import forms
from .models import *

class DoubtForm(forms.ModelForm):
	class Meta:
		model=Doubt
		fields='__all__'


class AnswerForm(forms.ModelForm):
	class Meta:
		model=Answer
		fields='__all__'