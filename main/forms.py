from .models import Ph
from django.forms import ModelForm, TextInput

class TaskForm(ModelForm):
    class Meta:
        model = Ph
        fields = ['title', 'task', 'number']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше Имя...'
            }),
            'task': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Курс, который выбрали...'
            }),
            'number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер телефона...',
                'input_type': 'tel',
                'pattern': r'^\+?[0-9]+$',
            }),
        }
