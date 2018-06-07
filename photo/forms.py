from photo.models import Album, Photo
from django.forms.models import inlineformset_factory

# 0525
# from django import forms

PhotoInlineFormSet = inlineformset_factory(Album, Photo,
    fields = ['image', 'title', 'year','description', 'money'],
    extra = 2)


# 0525
# class UploadImageForm(forms.Form):
#     image = forms.ImageField()
