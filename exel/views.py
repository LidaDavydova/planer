from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer
from django.urls import reverse
from .forms import RegisterFormView
from django.contrib.auth import authenticate, login
from django.views.generic.base import TemplateView
 
def main(request, name=''):
    return render(request, 'base.html', {'name': name})

class RegisterView(TemplateView):
    template_name = 'registration/register.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                User.objects.create_user(username, email, password)
                return redirect(reverse("login"))

        return render(request, self.template_name)

class ProfilePage(TemplateView):
    template_name = "registration/profile.html"

class LoginView(TemplateView):
    template_name = "registration/login.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("profile"))
            else:
                context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context)

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