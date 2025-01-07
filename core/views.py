from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Registration

# Create your views here.

def dashboard_view(request):
    return render(request, "core/dashboard.html")
def registration_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        sex = request.POST.get('sex')
        nic = request.POST.get('nic')
        certificate = request.POST.get('certificate')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        upload = request.FILES.get('upload')
        position = request.POST.get('position')

        if Registration.objects.filter(email=email).exists() or Registration.objects.filter(nic=nic).exists():
            messages.error(request, "Registration already exists")
            return render(request, "core/registration.html")

        Registration.objects.create(
            full_name=full_name,
            sex=sex,
            nic=nic,
            certificate=certificate,
            phone=phone,
            email=email,
            upload=upload,
            position=position
        )
        messages.success(request, 'Registration submitted successfully')
        return redirect('validation')
    return render(request, "core/registration.html")


def admin_dashboard(request):   
        registrations = Registration.objects.all()
        return render(request, 'core/admin_dashboard.html', {'registrations': registrations})
  
def admin_login(request):
    if request.POST.get('password') == 'Israel67564@':
        return redirect('admin')
    else:
        messages.error(request, "Invalid password")
    return render(request, 'core/adminlogin.html')    
    
def validation_view(request):
    return render(request, 'core/validation.html')    
