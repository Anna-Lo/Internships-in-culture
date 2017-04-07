from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.shortcuts import render, reverse

PROVINCE_CHOICES = (
('pustka', ''),
('pomorskie', 'pomorskie'),
('warmińsko-mazurskie', 'warmińsko-mazurskie'),
('podlaskie', 'podlaskie'),
('mazowieckie', 'mazowieckie'),
('lubelskie', 'lubelskie'),
('podkarpackie', 'podkarpackie'),
('małopolskie', 'małopolskie'),
('śląskie', 'śląskie'),
('opolskie', 'opolskie'),
('dolnośląskie', 'dolnośląskie'),
('lubuskie', 'lubuskie'),
('zachodniopomorskie', 'zachodniopomorskie'),
('wielkopolskie', 'wielkopolskie'),
('kujawsko-pomorskie', 'kujawsko-pomorskie'),
('łódzkie', 'łódzkie'),
('świętokrzyskie', 'świętokrzyskie'),
)

STUDIES_CHOICES = (
('0', ''),
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
    name = models.CharField(max_length=128, blank=True)
    description = models.TextField(blank=True)
    city = models.CharField(max_length=64, blank=True)
    address_street = models.CharField(max_length=128, blank=True)
    address_no = models.SlugField(max_length=4, blank=True)
    province = models.CharField(max_length=64, choices = PROVINCE_CHOICES, blank=True)

    def __str__(self):
        return "{}, {}".format(self.name, self.city)

    def get_absolute_url(self):
        return reverse('institution-info', kwargs={'institution_id': self.id})



class Offer(models.Model):
    name = models.CharField(max_length=256, help_text='Podaj stanowisko lub nazwę projektu')
    institution = models.ForeignKey(Institution)
    data_start = models.DateField()
    data_end = models.DateField()
    hours = models.IntegerField(validators=[MaxValueValidator(320), MinValueValidator(160)], default=160)
    duties = models.TextField()
    goal = models.CharField(max_length=1024)
    skills = models.TextField()
    studies = models.CharField(max_length=64, choices = STUDIES_CHOICES)
    studies_other = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse('offer-info', kwargs={'offer_id': self.id})
