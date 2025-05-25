from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.util import random_hex
from .forms import CustomUserCreationForm
from django.contrib.auth.models import Group

# Importamos lo necesario para generar la imagen
import qrcode
import qrcode.image.pil
import io
from base64 import b64encode

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            device = TOTPDevice.objects.create(
                user=user,
                name='default',
                confirmed=True,
                key=random_hex()
            )
            # Asignar al grupo "Solicitantes"
            grupo_solicitantes = Group.objects.get(name='solicitantes')
            grupo_solicitantes.user_set.add(user)
            return redirect('setup_mfa', device.id)
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def setup_mfa(request, device_id):
    device = TOTPDevice.objects.get(id=device_id)
    # Generamos la imagen con PIL en vez de PyPNG
    img = qrcode.make(
        device.config_url,
        image_factory=qrcode.image.pil.PilImage
    )
    # Guardamos la imagen en un buffer en memoria
    stream = io.BytesIO()
    # Ahora sí podemos usar 'PNG'
    img.save(stream, "PNG")
    # Codificamos a Base64
    data = b64encode(stream.getvalue()).decode()
    # Generamos el data URI
    qr_data_uri = f"data:image/png;base64,{data}"

    return render(request, 'accounts/setup_mfa.html', {
        'device': device,
        'qr_url': qr_data_uri,
    })
@login_required
def verify_token(request):
    if request.method == 'POST':
        token = request.POST.get('token')
        device = TOTPDevice.objects.get(user=request.user)
        if device.verify_token(token):
            return redirect('home')
        else:
            return render(request, 'accounts/verify_token.html', {'error': 'Token inválido'})
    return render(request, 'accounts/verify_token.html')
