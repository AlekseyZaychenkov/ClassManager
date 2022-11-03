from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


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


class Curator(models.Model):
    name = models.CharField(max_length=31, null=False, blank=False)
    last_name = models.CharField(max_length=31, null=True, blank=True)
    middle_name = models.CharField(max_length=31, null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)
    gender = models.CharField(max_length=6, choices=GENDERS)
    direction_of_training = models.OneToOneField(DirectionOfTraining, null=True, blank=True, on_delete=models.SET_NULL)


class AcademicDiscipline(models.Model):
    title = models.CharField(max_length=31, null=False, blank=False)
    direction_of_training = models.ForeignKey(DirectionOfTraining, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class StudyGroup(models.Model):
    number = models.CharField(max_length=31, null=False, blank=False)


class Student(models.Model):
    name = models.CharField(max_length=31, null=False, blank=False)
    last_name = models.CharField(max_length=31, null=True, blank=True)
    middle_name = models.CharField(max_length=31, null=True, blank=True)
    phone_number = PhoneNumberField(max_length=31, null=True, blank=True, unique=True)
    gender = models.CharField(max_length=6, choices=GENDERS)
    study_group = models.ForeignKey(StudyGroup, null=True, blank=True, on_delete=models.SET_NULL)
