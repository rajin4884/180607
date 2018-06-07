from django import forms

class CompanysSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')

'''
앨범 / 사진
'''

from companys.models import Album, Photo
from django.forms.models import inlineformset_factory

# 0525
# from django import forms

PhotoInlineFormSet = inlineformset_factory(Album, Photo,
    fields = ['image', 'title'],
    extra = 2)
