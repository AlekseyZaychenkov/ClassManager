# -*- coding: utf-8 -*-
import logging

from django import forms

# from manager.models import Image
from manager.validators import validate_file_extension
from manager.utils import delete_image

from django import forms
from django.contrib import admin
from manager.models import DirectionOfTraining


log = logging.getLogger(__name__)


# class DirectionOfTrainingForm(forms.ModelForm):
#
#     class Meta:
#         model = DirectionOfTraining
#         fields = ['title']
#
# class DirectionOfTrainingAdmin(admin.ModelAdmin):
#     fields = ['title']
#     form = DirectionOfTrainingForm



# class ImageCreateForm(forms.ModelForm):
#     image_field = forms.ImageField(widget=forms.ClearableFileInput(), validators=[validate_file_extension])
#     text = forms.CharField(widget=forms.Textarea(attrs={"rows": 3, "cols": 10}), required=False)
#
#     def set_gallery(self, gallery):
#         image = self.instance
#         image.gallery = gallery
#         self.instance = image
#
#     def save(self, commit=True):
#         image = self.instance
#         if commit:
#             image.save()
#
#         return image
#
#     class Meta:
#         model = Image
#         exclude = ('gallery', )


# class ImageEditForm(forms.ModelForm):
#     image_field = forms.ImageField(widget=forms.ClearableFileInput(), validators=[validate_file_extension], required=False)
#     text = forms.CharField(widget=forms.Textarea(attrs={"rows": 3, "cols": 10}), required=False)
#
#     def save(self, commit=True):
#         image = self.instance
#         if commit:
#             image.save()
#
#         return image
#
#     class Meta:
#         model = Image
#         exclude = ('image_field', 'text', 'gallery',)


# class ImageDeleteForm(forms.Form):
#     image_id = forms.CharField(required=True)
#
#     def delete(self):
#         image_id = self.data["image_id"]
#         image = Image.objects.get(id=image_id)
#         delete_image(image)
