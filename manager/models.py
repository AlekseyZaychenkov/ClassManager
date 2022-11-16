from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from account.models import Account

MALE = 'M'
FEMALE = 'F'
GENDERS = [
    (MALE, 'male'),
    (FEMALE, 'female'),
]


class DirectionOfTraining(models.Model):
    title = models.CharField(max_length=31, null=False, blank=False)

    def __str__(self):
        return self.title


class Curator(Account):
    name = models.CharField(max_length=31, null=False, blank=False)
    last_name = models.CharField(max_length=31, null=True, blank=True)
    middle_name = models.CharField(max_length=31, null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)
    gender = models.CharField(max_length=6, null=True, blank=True, choices=GENDERS)
    direction_of_training = models.OneToOneField(DirectionOfTraining, on_delete=models.CASCADE)


class AcademicDiscipline(models.Model):
    title = models.CharField(max_length=31, null=False, blank=False)
    direction_of_training = models.ForeignKey(DirectionOfTraining, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class StudyGroup(models.Model):
    number = models.CharField(max_length=31, null=False, blank=False)
    direction = models.ForeignKey(DirectionOfTraining, on_delete=models.CASCADE)

    class Meta:
        ordering = 'number',


class Student(models.Model):
    name = models.CharField(max_length=31, null=False, blank=False)
    last_name = models.CharField(max_length=31, null=True, blank=True)
    middle_name = models.CharField(max_length=31, null=True, blank=True)
    phone_number = PhoneNumberField(max_length=31, null=True, blank=True, unique=False)
    gender = models.CharField(max_length=6, choices=GENDERS)
    study_group = models.ForeignKey(StudyGroup, null=True, blank=True, on_delete=models.SET_NULL)
    direction = models.ForeignKey(DirectionOfTraining, on_delete=models.CASCADE)

    class Meta:
        ordering = 'last_name', 'name', 'middle_name',
