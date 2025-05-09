from django.shortcuts import render
from django.utils import timezone
from datetime import date
from .forms import BirthdayForm

def birthday_form_view(request):
    result = None
    
    if request.method == 'POST':
        form = BirthdayForm(request.POST)
        if form.is_valid():
            birth_date = form.cleaned_data['birth_date']
            today = date.today()
            
            # Calculate years passed
            years = today.year - birth_date.year
            
            # Adjust if birthday hasn't occurred yet this year
            if (today.month, today.day) < (birth_date.month, birth_date.day):
                years -= 1
            
            # Calculate the exact years with decimal precision
            # Create a date for this year's birthday
            this_year_birthday = date(today.year, birth_date.month, birth_date.day)
            
            # If birthday hasn't occurred yet this year, use last year's birthday
            if this_year_birthday > today:
                this_year_birthday = date(today.year - 1, birth_date.month, birth_date.day)
            
            # Next birthday
            next_birthday = date(this_year_birthday.year + 1, birth_date.month, birth_date.day)
            
            # Calculate days since last birthday
            days_since_last_birthday = (today - this_year_birthday).days
            
            # Calculate total days in this year (accounts for leap years)
            days_in_year = (next_birthday - this_year_birthday).days
            
            # Calculate the decimal part
            decimal_part = days_since_last_birthday / days_in_year
            
            # Final result with 2 decimal places
            result = round(years + decimal_part, 2)
            
            return render(request, 'birthday_app/result.html', {
                'form': form,
                'result': result,
                'birth_date': birth_date
            })
    else:
        form = BirthdayForm()
    
    return render(request, 'birthday_app/birthday_form.html', {'form': form, 'result': result})
