from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

PROVINCE_CHOICES = (
('pom', 'pomorskie'),
('wm', 'warmińsko-mazurskie'),
('pod', 'podlaskie'),
('maz', 'mazowieckie'),
('lbl', 'lubelskie'),
('pdk', 'podkarpackie'),
('mp', 'małopolskie'),
('sl', 'śląskie'),
('op', 'opolskie'),
('dsl', 'dolnośląskie'),
('lub', 'lubuskie'),
('zp', 'zachodniopomorskie'),
('wkp', 'wielkopolskie'),
('kpo', 'kujawsko-pomorskie'),
('ldz', 'łódzkie'),
('sw', 'świętokrzyskie'),
)

STUDIES_CHOICES = (
('1', 'animacja kultury'),
('2', 'antropologia'),
('3', 'archeologia'),
('4', 'bibliotekoznawstwo'),
('5', 'dziennikarstwo'),
('6', 'filologia angielska'),
('7', 'filologia francuska'),
('8', 'filologia polska'),
('9', 'filologia romańska'),
('10', 'filozofia'),
('11', 'grafika'),
('12', 'historia'),
('13', 'historia sztuki'),
('14', 'konserwacja zabytków'),
('15', 'kulturoznawstwo'),
('16', 'muzykologia'),
('17', 'pedagogika'),
('18', 'psychologia'),
('19', 'socjologia'),
('20', 'teatrologia'),
('21', 'zarządzanie kulturą'),
)

class Institution(models.Model):
    user = models.OneToOneField(User, unique=True)
    name = models.CharField(max_length=128)
    description = models.TextField()
    city = models.CharField(max_length=64)
    province = models.CharField(max_length=64, choices = PROVINCE_CHOICES)

class Offer(models.Model):
    institution = models.ForeignKey(Institution)
    data_start = models.DateField()
    data_end = models.DateField()
    hours = models.IntegerField(validators=[MaxValueValidator(320), MinValueValidator(160)], default=160)
    duties = models.TextField()
    goal = models.CharField(max_length=1024)
    skills = models.TextField()
    studies = models.CharField(max_length=64, choices = STUDIES_CHOICES)
    studies_other = models.CharField(max_length=64, blank=True)

class Student(models.Model):
    user = models.OneToOneField(User, unique=True)
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
