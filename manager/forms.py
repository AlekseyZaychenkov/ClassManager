# -*- coding: utf-8 -*-
import logging

from phonenumber_field.modelfields import PhoneNumberField
from django import forms
from manager.models import DirectionOfTraining, Student, GENDERS, StudyGroup

log = logging.getLogger(__name__)


class StudyGroupCreateForm(forms.ModelForm):
    number = forms.CharField(required=True)
    direction_id = forms.CharField(required=True)

    def save(self, commit=True):
        group = self.instance

        direction = DirectionOfTraining.objects.get(id=self.cleaned_data["direction_id"])
        group.direction = direction

        if commit:
            direction.save()
            group.save()

    class Meta:
        model = StudyGroup
        exclude = ('direction',)


class StudyGroupeEditForm(forms.ModelForm):
    id = forms.CharField(required=True)
    number = forms.CharField(required=True)

    def save(self, commit=True):
        group = StudyGroup.objects.get(id=self.cleaned_data["id"])

        group.number = self.cleaned_data["number"]

        if commit:
            group.save()

    class Meta:
        model = StudyGroup
        exclude = ('direction',)


class StudyGroupDeleteForm(forms.Form):
    group_id = forms.CharField(required=True)

    def delete(self):
        group_id = self.data["group_id"]
        if StudyGroup.objects.filter(id=group_id).exists():
            StudyGroup.objects.get(id=group_id).delete()
        else:
            log.error(f"No student with id='{group_id}' in data base!")


class StudentCreateForm(forms.ModelForm):
    name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    middle_name = forms.CharField(required=False)
    phone_number = PhoneNumberField()
    gender = forms.ChoiceField(choices=GENDERS)
    direction_id = forms.CharField(required=True)

    def save(self, commit=True):
        student = self.instance

        direction = DirectionOfTraining.objects.get(id=self.cleaned_data["direction_id"])
        student.direction = direction

        if commit:
            direction.save()
            student.save()

    class Meta:
        model = Student
        exclude = ('study_group', 'direction',)


class StudentEditForm(forms.ModelForm):
    id = forms.CharField(required=True)
    name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    middle_name = forms.CharField(required=False)
    phone_number = PhoneNumberField()
    gender = forms.ChoiceField(choices=GENDERS)

    def save(self, commit=True):
        student = Student.objects.get(id=self.cleaned_data["id"])

        student.name = self.cleaned_data["name"]
        student.last_name = self.cleaned_data["last_name"]
        student.middle_name = self.cleaned_data["middle_name"]
        student.phone_number = self.cleaned_data["phone_number"]
        student.gender = self.cleaned_data["gender"]

        if commit:
            student.save()

    class Meta:
        model = Student
        exclude = ('study_group', 'direction',)


class StudentAddToGroupForm(forms.Form):
    student_id = forms.CharField(required=True)

    def add(self, group_id):
        student_id = self.data["student_id"]

        if not group_id:
            log.error(f"No group was selected. Excluding student from current group.")

            student = Student.objects.get(id=student_id)
            group = student.study_group
            student.study_group = None
            student.save()
            group.save()
            return

        if not StudyGroup.objects.filter(id=group_id).exists():
            log.error(f"No group with id='{group_id} exists in data base!")
            return

        if Student.objects.filter(id=student_id).exists():
            group = StudyGroup.objects.filter(id=group_id).get()
            student = Student.objects.get(id=student_id)
            student.study_group = group
            student.save()
            group.save()
        else:
            log.error(f"No student with id='{student_id}' exists in data base!")


class StudentDeleteForm(forms.Form):
    student_id = forms.CharField(required=True)

    def delete(self):
        student_id = self.data["student_id"]
        if Student.objects.filter(id=student_id).exists():
            Student.objects.get(id=student_id).delete()
        else:
            log.error(f"No student with id='{student_id}' in data base!")
