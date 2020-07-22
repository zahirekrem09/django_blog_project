from django.contrib.auth.models import AbstractUser
from django.db import models
from blog.choices import (GenderChoices,
                          MartialStatusChoices,
                          EducationalStatusChoices,
                          ProfessionChoices
                          )


class Interest(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name


class User(AbstractUser):
  birthday = models.DateField(null=True)
  phone_number = models.CharField(max_length=15, null=True)
  gender = models.PositiveIntegerField(
      null=True, choices=GenderChoices.CHOICES)
  marital_status = models.PositiveIntegerField(
      null=True, choices=MartialStatusChoices.CHOICES)
  educational_status = models.PositiveIntegerField(
      null=True, choices=EducationalStatusChoices.CHOICES)
  profession = models.PositiveIntegerField(
      null=True, choices=ProfessionChoices.CHOICES)
  interests = models.ManyToManyField(to=Interest)

  profile_image = models.FileField(
      upload_to='images/', blank=True, null=True, verbose_name="Profil İmage", default="/static/img/indir.jpg")

  class Meta:
    verbose_name = "User"

  # @property
  # def profile_image(self):
  #   return "/static/img/indir.jpg"
