from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect

# Signup view
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log in the user after signup
            next_url = request.POST.get('next', None)  # Get 'next' parameter if it exists
            if next_url:
                return redirect(next_url)  # Redirect to the 'next' URL
            return redirect('movie:list')  # Default redirect after signup
    else:
        form = UserCreationForm()

    # Check if there's a 'next' parameter in the GET request and pass it to the form
    context = {"form": form}
    if 'next' in request.GET:
        context['next'] = request.GET['next']

    return render(request, 'accounts/signup.html', context)

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Authenticate the user
            login(request, user)  # Log in the user
            next_url = request.POST.get('next', None)  # Get 'next' parameter if it exists
            if next_url:
                return redirect(next_url)  # Redirect to the 'next' URL
            return redirect('movie:list')  # Default redirect after login
    else:
        form = AuthenticationForm()

    # Check if there's a 'next' parameter in the GET request and pass it to the form
    context = {"form": form}
    if 'next' in request.GET:
        context['next'] = request.GET['next']

    return render(request, 'accounts/login.html', context)

# Logout view
def logout_view(request):
    if request.method == "POST":
        logout(request)  # Log out the user
        return redirect('movie:list')  # Redirect to the movie list after logout
