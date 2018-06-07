from django import forms
from .models import CraftPost, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CraftForm(forms.ModelForm):

	class Meta:
		model = CraftPost
		fields = ('title', 'photo','career','money', 'text', 'link')

		widgets = {
            'title': forms.TextInput(
                attrs={
                    # 'class': 'form-control',
                }
            ),
            'career': forms.TextInput(
                attrs={
                    # 'class': 'form-control',
                }
            ),
            # 'money': forms.NumberInput(
            #     attrs={
            #         # 'class': 'form-control',
            #     }
            # ),
            'text': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            ),
            'link': forms.URLInput(
                attrs={
                    # 'class': 'form-control',
                }
            ),
        }
		labels={
            'title': '멘토링명',
            'photo': '사진',
			'career': '경력',
			'money': '금액',
			'text': '멘토링 내용',
			'link': '참고 url',
			}

	# class Media:
	# 	js = ('/media/tinymce/jscripts/tiny_mce/tiny_mce.js',
    #             '/sitemedia/js/tinymce_setup.js',)

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ( 'author', 'text',)

	# class Media:
	# 	js = ('/media/tinymce/jscripts/tiny_mce/tiny_mce.js',
    #             '/sitemedia/js/tinymce_setup.js',)
