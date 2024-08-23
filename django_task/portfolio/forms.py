from django import forms
from .models import portfolio_detail

class PortfolioDetailForm(forms.ModelForm):
    class Meta:
        model = portfolio_detail
        fields = ['first_name', 'last_name', 'age', 'city', 'content', 'read_more', 'event_date', 'event_time', 'img_title', 'img_url']
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date'}),
            'event_time': forms.TimeInput(attrs={'type': 'time'}),
        }
