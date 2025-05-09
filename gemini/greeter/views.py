from django.shortcuts import render
from .forms import NameForm

def greet_user(request):
    user_name = None  # Variable to hold the name if submitted

    if request.method == 'POST':
        # Create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # Check whether it's valid:
        if form.is_valid():
            # Process the data in form.cleaned_data as required
            user_name = form.cleaned_data['name']
            # We don't necessarily need to redirect here for this simple case.
            # We'll just render the same template but pass the user_name.
            # Create a new empty form instance for the template after successful POST
            form = NameForm() # Show a fresh form below the greeting
    else:
        # If it's a GET (or any other method), create a blank form
        form = NameForm()

    # Prepare the context to pass to the template
    context = {'form': form, 'user_name': user_name,}
    # Render the template with the context
    return render(request, 'greeter/greet.html', context)
