from django import forms
from videos.models import *

class VideoForm(forms.ModelForm):
	class Meta:
		model = Video
		fields = ('name','theme','video')
