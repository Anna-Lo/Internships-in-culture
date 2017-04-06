"""Internships URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from intern_app.views import (
AddInstitutionView,
AddOfferView,
InstitutionInfoView,
LoginView,
LogoutView,
MainView,
OfferInfoView,
OffersByInstitutionView,
RegisterView,
RegisteredView,
SearchOffersView,
ShowInstitutionsView,
ShowOffersView,
WelcomeView,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', WelcomeView.as_view(), name='welcome'),
    url(r'^register/', RegisterView.as_view(), name='register'),
    url(r'^registered/', RegisteredView.as_view(), name='registered'),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^add_institution/', AddInstitutionView.as_view(), name='add-institution'),
    url(r'^institution_info/(?P<institution_id>(\d)+)$', InstitutionInfoView.as_view(), name='institution-info'),
    url(r'^show_institutions/', ShowInstitutionsView.as_view(), name='show-institutions'),
    url(r'^main/', MainView.as_view(), name='main'),
    url(r'^add_offer/', AddOfferView.as_view(), name='add-offer'),
    url(r'^offer_info/(?P<offer_id>(\d)+)', OfferInfoView.as_view(), name='offer-info'),
    url(r'^show_offers/', ShowOffersView.as_view(), name='show-offers'),
    url(r'^search_offers/', SearchOffersView.as_view(), name='search-offer'),
    url(r'^institution_info/(?P<institution_id>(\d)+)/show_offers', OffersByInstitutionView.as_view(), name='offers-by-institutions'),
]
