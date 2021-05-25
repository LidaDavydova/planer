from django import forms
from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer
from django.views.generic.edit import FormView

class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "login.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)

class RegistrForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'password')
        
        widgets = {
            "first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
                }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
                }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
                })
            }


class InputForm(forms.Form):

   

    first_name = forms.CharField(max_length = 50)

    last_name = forms.CharField(max_length = 50)

    password = forms.CharField(widget = forms.PasswordInput())