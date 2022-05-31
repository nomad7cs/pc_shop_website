from django.db import models


class Computer(models.Model):
  title = models.CharField(max_length=200)
  price = models.FLoatField()
  manufacturer_name = models.CharField(max_length=200)
  model_name = models.CharField(max_length=200)
  registration_date = models.DateTimeField('Date registered')
  parts = models.ManyToManyField(ComputerPart)

  def __str__(self):
    return self.title


class ComputerPart(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=200)
  price = models.FLoatField()
  manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE,)
  model_name = models.CharField(max_length=200)

  def __str__(self):
    return self.name


class Manufacturer(models.Model):
  full_name = models.CharField(max_length=200)
  short_name = models.CharField(max_length=200)
  contact = models.CharField(max_length=200)

  def __str__(self):
    return self.full_name
