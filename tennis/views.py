from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, FormView
from .models import ContactForm
from .forms import ContactUsForm
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class ContactPageView(CreateView):
    model = ContactForm
    template_name = "contact.html"
    form_class = ContactUsForm
    success_url = reverse_lazy("home")
