from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.core.mail import send_mail
from .forms import RegistrationForm, ProfileForm

# Log out function
def logout_view(request):
    """Log the user out."""
    logout(request)

    return redirect('main_app:index')
    
# Registration function
def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # Display blank registration form
        registration_form = RegistrationForm()
        profile_form = ProfileForm()
    else:
        # Process the completed forms
        registration_form = RegistrationForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        if registration_form.is_valid() and profile_form.is_valid():
            # Save the new user to the database
            new_user = registration_form.save(commit=False)
            new_user.set_password(registration_form.cleaned_data['password'])
            new_user.save()
            # Save the new user profile to the database
            new_profile = profile_form.save(commit=False)
            new_profile.username = new_user
            new_profile.save()
            # Log user in and redirect to the home page
            login(request, new_user)
            return redirect('main_app:index')
        
    context = {'registration_form': registration_form, 'profile_form': profile_form}
    return render(request, 'users/register.html', context)
