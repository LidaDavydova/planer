from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer, Brief, Fileexel
from django.urls import reverse
from .forms import RegisterFormView
from django.contrib.auth import authenticate, login
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.conf import settings
from django.core.files.storage import FileSystemStorage
 
def main(request, super_us = False):
    #if not auth_user.objects.get()
    if super_us == 'True':
        return render(request, 'base.html', {'body':'on'})
    return render(request, 'base.html', {'body':'off'})

def prepare(request):
    return render(request, 'prepare_calculation/prepare')

class RegisterView(TemplateView):
    template_name = 'registration/register.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')
            if password == password2:
                User.objects.create_user(username=username, email=email, password=password)
                super_us = User.objects.get(username=username, email=email)
                return main(request, super_us.is_superuser)
        return render(request, self.template_name)

class ProfilePage(TemplateView):
    template_name = "registration/profile.html"
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            return redirect(reverse("main"))
        return render(request, self.template_name)

class LoginView(TemplateView):
    template_name = "registration/login.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            super_us = User.objects.get(username=username, password=password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                #login(request, user)
                return render(request, "registration/profile.html", {'user':super_us.is_superuser})
            else:
                context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context)
    
class Prepare_calc(TemplateView):
    template_name = "prepare_calculation/prepare.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            budget = request.POST.get('budget')
            landing_page = request.POST.get('landing_page')
            description = request.POST.get('description')
            UTP = request.POST.get('UTP')
            competitors = request.POST.get('competitors')
            terms = request.POST.get('terms')
            geography = request.POST.get('geography')
            KPI = request.POST.get('KPI')
            audience = request.POST.get('audience')
            suggestions = request.POST.get('suggestions')
            companies_before = request.POST.get('companies_before')
            who_prep_materials = request.POST.get('who_prep_materials')
            instrument = request.POST.get('instrument')
            official_list = request.POST.get('official_list')
            CRM = request.POST.get('CRM')
            
            Brief.objects.create(sum_all=budget, landing_page=landing_page, description=description,
                                 UTP=UTP, competitors=competitors, terms=terms, geography=geography,
                                 KPI=KPI, audience=audience, suggestions=suggestions,
                                 companies_before=companies_before, who_prep_materials=who_prep_materials,
                                 instrument=instrument, official_list=official_list,
                                 CRM=CRM)

        return render(request, self.template_name, context)

def calculate(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'prepare_calculation/calculate.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'prepare_calculation/calculate.html')

class Calc(ListView):
    model = Fileexel
    template_name = 'prepare_calculation/calculate.html'
    
class Download_calc(TemplateView):
    template_name = "download_calc.html"
    
    def dispatch(self, request, *args, **kwargs):
        return render(request, self.template_name, {'details':Fileexel.objects.all()})

'''
def registr(request):
    error = ''
    if request.method == 'POST':
        form = RegistrForm(request.POST)
        if form.is_valid():
            d = form.cleaned_data
            if not Customer.objects.filter(
                                        first_name=d['first_name'], 
                                        last_name=d['last_name'], 
                                        password=d['password']):
                form.save()
                return main(request, Customer.objects.get(first_name=d['first_name'], 
                                                          last_name=d['last_name'], 
                                                          password=d['password']))
        else:
            error = "Plese, check what you've written"
            
    form = RegistrForm()
    data = {
        'form': form,
        'error': error
        }
    return render(request, 'regitration/login.html', data)
'''