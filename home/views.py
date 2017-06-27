from django.shortcuts import render
from .models import SliderImage


def index_view(request):
    sliders = SliderImage.objects.all()
    return render(request, 'index.html', {'sliders': sliders})
# Create your views here.
