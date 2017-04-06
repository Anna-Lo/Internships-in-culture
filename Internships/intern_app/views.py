from django.shortcuts import render
# from intern_app.forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views import View
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .forms import LoginForm, AddInstitutionForm, AddOfferForm, RegisterForm, SearchOffersForm
from .models import Institution, Offer



# Create your views here.
class WelcomeView(View):
    def get(self, request):
        return render(request, 'intern_app/welcome.html')

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        ctx = {"form": form}
        return render(request, 'intern_app/register_form.html', ctx)

    def post(self, request):
        form = RegisterForm(request.POST)
        ctx = {'form': form}
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('registered'))
        else:
            return HttpResponseRedirect(reverse('welcome'))

# class RegisterView(View):
#     def get(self, request):
#         form = UserCreationForm()
#         ctx = {"form": form}
#         return render(request, 'intern_app/register_form.html', ctx)
#
#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             return HttpResponseRedirect(reverse('registered'))
#         else:
#             return HttpResponseRedirect(reverse('welcome'))

class RegisteredView(View):
    def get(self, request):
        return render(request, 'intern_app/registered.html')

class LoginView(View):
    def get(self, request):
        ctx = {'form': LoginForm()}
        return render(request, 'intern_app/login.html', ctx)

    def post(self, request):
        form = LoginForm(data=request.POST)
        ctx = {'form': form}
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            return HttpResponseRedirect(reverse('show-institutions'))
            #return HttpResponseRedirect(reverse('show-institutions'))
        else:
            return render(request, 'intern_app/login.html', ctx)

class LogoutView(View):
    def get(self, request):
        request.user
        logout(request)
        return HttpResponseRedirect(reverse('welcome'))

def raise_unless_unauthenticated(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('login'))

class AddInstitutionView(LoginRequiredMixin, View):
    #raise_exception = raise_unless_unauthenticated
    # def raise_unless_unauthenticated(request):
    #     if not request.user.is_authenticated():
    #         return HttpResponseRedirect(reverse('login'))

    def get(self, request):
        ctx = {'form': AddInstitutionForm()}
        return render(request, 'intern_app/institution_form.html', ctx)

    def post(self, request):
        form = AddInstitutionForm(request.POST)
        ctx = {'form': form}
        if form.is_valid():
            institution=form.save()
            user = form.cleaned_data['user']
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            city = form.cleaned_data['city']
            address_street = form.cleaned_data['address_street']
            address_no = form.cleaned_data['address_no']
            province = form.cleaned_data['province']
            userprofile = Institution.objects.create(name=name, description=description, city=city, address_street=address_street,
                                        address_no=address_no, province=province)
            return HttpResponseRedirect(institution.get_absolute_url())
        return render(request, 'intern_app/institution_form.html', ctx)
    # template_name = 'institution_form.html'
    # form_class = AddInstitutionForm
    # model = Institution
    # fields = '__all__'

class InstitutionInfoView(View):
    def get(self, request, institution_id):
        institution = Institution.objects.get(pk=institution_id)
        ctx = {'institution': institution}
        return render(request, 'intern_app/institution_info.html', ctx)

class ShowInstitutionsView(View):
    def get(self, request):
        institutions = Institution.objects.all()
        ctx = {'institutions': institutions}
        return render(request, 'intern_app/institutions.html', ctx)

class MainView(View):
    def get(self, request):
        return render(request, 'intern_app/main.html')

class AddOfferView(LoginRequiredMixin, View):

    def get(self, request):
        form = AddOfferForm()
        ctx = {'form': form}
        return render(request, 'intern_app/offer_form.html', ctx)

    def post(self, request):
        form = AddOfferForm(request.POST)
        ctx = {'form': form}
        if form.is_valid():
            offer = form.save()
            name = form.cleaned_data['name']
            institution = form.cleaned_data['institution']
            data_start = form.cleaned_data['data_start']
            data_end = form.cleaned_data['data_end']
            hours = form.cleaned_data['hours']
            duties = form.cleaned_data['duties']
            goal = form.cleaned_data['goal']
            skills = form.cleaned_data['skills']
            studies = form.cleaned_data['studies']
            studies_other = form.cleaned_data['studies_other']
            Offer.objects.create(name=name, institution=institution, data_start=data_start, data_end=data_end, hours=hours,
                                        duties=duties, goal=goal, skills=skills, studies=studies, studies_other=studies_other)
            return HttpResponseRedirect(offer.get_absolute_url())
        return render(request, 'intern_app/offer_form.html', ctx)

class OfferInfoView(View):
    def get(self, request, offer_id):
        offer = Offer.objects.get(pk=offer_id)
        ctx = {'offer': offer}
        return render(request, 'intern_app/offer_info.html', ctx)

class ShowOffersView(View):
    def get(self, request):
        offers = Offer.objects.all()
        ctx = {'offers': offers}
        return render(request, 'intern_app/show_offers.html', ctx)

class SearchOffersView(View):
    def get(self, request):
        form = SearchOffersForm()
        ctx = {'form': SearchOffersForm()}
        return render(request, 'intern_app/search_offers.html',ctx )

    def post(self, request):
        form = SearchOffersForm(request.POST)
        ctx = {'form': form}
        if form.is_valid():
            institution_name = form.cleaned_data['institution_name']
            institution_city = form.cleaned_data['institution_city']
            institution_province = form.cleaned_data['institution_province']
            offer_studies = form.cleaned_data['offer_studies']
            institutions_by_name = Institution.objects.filter(name__icontains=institution_name)
            offers_by_institution_name = Offer.objects.filter(institution=institutions_by_name)
            institutions_by_city = Institution.objects.filter(city__icontains=institution_city)
            institutions_by_province = Institution.objects.filter(province=institution_province)
            offers_by_studies = Offer.objects.filter(studies=offer_studies)
            ctx = {'institutions_by_name': institutions_by_name,
                    'institutions_by_city': institutions_by_city,
                    'institutions_by_province': institutions_by_province,
                    'offers_by_studies': offers_by_studies,
                    'offers_by_institution_name': offers_by_institution_name,
                    'form': form}
            return render(request, 'intern_app/search_results.html',ctx)

class OffersByInstitutionView(View):
    def get(self, request, institution_id):
        institution = Institution.objects.get(pk=institution_id)
        offers = Offer.objects.filter(institution=institution_id)
        ctx = {'institution': institution, 'offers': offers}
        return render(request, 'intern_app/offers_by_institution.html', ctx)
