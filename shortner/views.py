import random
import string
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import ShortUrl

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def home(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']
        short_code = generate_short_code()
        short_url, created = ShortUrl.objects.get_or_create(original_url=original_url, short_code=short_code)
        return render(request, 'shortener/home.html', {'short_url': short_url})
    return render(request, 'shortener/home.html')

def redirect_url(request, short_code):
    short_url = get_object_or_404(ShortUrl, short_code=short_code)
    return redirect(short_url.original_url)
