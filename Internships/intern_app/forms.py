from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import Institution, Offer, PROVINCE_CHOICES, STUDIES_CHOICES

# from intern_app.models import Profile
# from django.contrib.auth.hashers import make_password

# class AddInstitutionForm(forms.ModelForm):
#     class Meta:
#         model = Institution
#         fields = '__all__'

class AddInstitutionForm(forms.ModelForm):
    #user = forms.CharField(max_length=64, label='Nazwa użytkownika')
    name = forms.CharField(max_length=128, label='Nazwa instytucji', required=True)
    description = forms.CharField(widget=forms.Textarea, label='Opis działalności', required=True)
    city = forms.CharField(max_length=64, label ='Miejscowośc', required=True)
    address_street = forms.CharField(max_length=128, label='Ulica', required=True)
    address_no = forms.SlugField(max_length=4, label='Numer domu', required=True)
    province = forms.CharField(widget=forms.Select(choices=PROVINCE_CHOICES), label='Województwo', required=True)

    class Meta:
        model = Institution
        fields = '__all__'

class AddOfferForm(forms.ModelForm):
    name = forms.CharField(max_length=256, label='Stanowisko lub nazwa projektu')
    institution = forms.ModelChoiceField(queryset=Institution.objects.all(),label='Instytucja')
    data_start = forms.DateField(label='Początek stażu')
    data_end = forms.DateField(label='Koniec stażu')
    hours = forms.IntegerField(label='Długość stażu w godz.')
    duties = forms.CharField(widget=forms.Textarea, label='Obowiązki stażysty')
    goal = forms.CharField(max_length=1024, label='Cel stażu')
    skills = forms.CharField(widget=forms.Textarea, label='Umiejętności, jakie nabędzie stażysta')
    studies = forms.CharField(max_length=64, widget=forms.Select(choices=STUDIES_CHOICES), label='Preferowany kierunek studiów')
    studies_other = forms.CharField(max_length=64, label='Preferowany kierunek studiów(inny)')

    class Meta:
        model = Offer
        fields = '__all__'

class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=64, label='Użytkownik')
    password = forms.CharField(widget=forms.PasswordInput, label='Hasło')
    password2 = forms.CharField(widget=forms.PasswordInput, label = 'Powtórz hasło')

    class Meta:
        model = User
        fields = ('username', 'password', 'password2')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['password'].widget = forms.PasswordInput()

    def clean(self):
        cleaned_data = super().clean()
        raw_password = cleaned_data['password']
        cleaned_data['password'] = make_password(raw_password)
        return cleaned_data

    # def save(self, commit=True):
    #     user = super(RegisterForm, self).save(commit=False)
    #     username = cleaned_data["username"]
    #     password = cleaned_data['password']
    #     password2 = cleaned_data['password2']
    #     if password == password2:
    #         if commit:
    #             user.save()
    #             return user
    #     else:
    #         raise forms.ValidationError('Nieprawidłowe dane logowania')

class LoginForm(forms.Form):
    użytkownik = forms.CharField(max_length=64)
    hasło = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        login = cleaned_data['użytkownik']
        password = cleaned_data['hasło']
        user = authenticate(username=login, password=password)
        if user is None:
            raise forms.ValidationError('Nieprawidłowe dane logowania')

        cleaned_data['user'] = user
        return cleaned_data

class SearchOffersForm(forms.Form):
    institution_name = forms.CharField(max_length=128, label='Nazwa instytucji', required=False)
    institution_city = forms.CharField(max_length=64, label ='Miejscowość', required=False)
    institution_province = forms.CharField(widget=forms.Select(choices=PROVINCE_CHOICES), label='Województwo', required=False)
    offer_studies = forms.CharField(max_length=64, widget=forms.Select(choices=STUDIES_CHOICES), label='Preferowany kierunek studiów', required=False)
