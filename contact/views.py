from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


# Create your views here.

def emailView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            form.save()
            messages.success(
                request, 'We have received your email successsfully')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {"form": form})
