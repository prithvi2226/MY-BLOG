from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	#modelform allows us to create a form
	class Meta:
		model = Post
		fields = ('title', 'title_tag', 'author', 'body')

		widgets = {
			'title': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Add title'}),
			'title_tag': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Add title tag'}),
			'author': forms.Select(attrs = {'class': 'form-control'}),
			'body': forms.Textarea(attrs = {'class': 'form-control', 'placeholder': 'YOUR BLOG'})
		}