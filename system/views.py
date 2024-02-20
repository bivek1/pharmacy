from io import BytesIO
import re
from urllib.parse import urlparse
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
import qrcode
def LoginView(request):
    if request.method == 'POST':
        username = request.POST['email_user']
        password = request.POST['password']

        log= authenticate(request, username = username, password = password)

        if log != None:
            login(request, log)
            return HttpResponseRedirect(reverse('system:dashboard'))
        else:
            messages.error(request, "Failed to authenticate user")

    
    return render(request, "login.html")


@login_required
def Dashboard(request):
    return render(request, "customer/dashboard.html")


@login_required
def AddMedicine(request):
    form = MedicineForm(request.POST or None)

    medicine = Medicine.objects.all().order_by('-id')

    dist = {
        'form':form,
        'medicine':medicine
    }

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added medicine")
        else:
            messages.success(request, "Something went wrong")
    return render(request, "customer/addMedicine.html", dist)


def qrView(request):
    return render(request, "customer/qr.html")


def generateQR(request):

    if request.method == 'POST':
        text = request.POST.get('text')
        print(text)
        
        qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")


        image_io = BytesIO()
        img.save(image_io, format='PNG')

        cleaned_path = re.sub(r'[^a-zA-Z0-9\s]', '', urlparse(text).path)

        # Split the path into words and limit to 30 words
        words = cleaned_path.split()
        limited_words = ' '.join(words[:30])

        qr_object = QR.objects.create(name= limited_words)
        qr_object.image.save(f'{limited_words}.png', ContentFile(image_io.getvalue()))


        return JsonResponse({'path':qr_object.image.url})

def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('system:login'))