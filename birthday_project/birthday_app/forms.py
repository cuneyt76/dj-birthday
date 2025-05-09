from django import forms

class BirthdayForm(forms.Form):
    birth_date = forms.DateField(
        label='Your Birthday',
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text='Enter your birth date'
    )