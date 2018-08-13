from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Farm, Expenses, farm_production


class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2',)

class FarmForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FarmForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model=Farm
        fields = ['name', 'type', 'size','location']
        exclude = ["farmer"]



class ExpenseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model=Expenses
        fields=['farm','amount', 'description']



class ProductionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model=farm_production
        fields=['farm','year','production_amount', 'dateRecorded']
        exclude = ["farmer"]




