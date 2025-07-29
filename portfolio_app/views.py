from django.shortcuts import render, redirect
from .models import Project
from .forms import ContactForm

def home(request):
    projects = Project.objects.all()
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # refresh the page

    return render(request, 'index.html', {
        'projects': projects,
        'form': form
    })
