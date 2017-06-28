from django.shortcuts import render
from .models import SliderImage
from post.models import Post, Contact
from gallery.models import MainGallery
from service.models import *
from contact.models import *


def index_view(request):
    sliders = SliderImage.objects.all()
    posts = Post.objects.all()[:3]
    contacts = Contact.objects.all()
    galleries = MainGallery.objects.all()[:5]
    sstatics = ServiceStatic.objects.all()
    sdynamics = ServiceDynamic.objects.all()
    informations = ContactInfo.objects.all()
    socials = SocialNetwork.objects.all()
    return render(request, 'index.html', {
        'sliders': sliders,
        'posts': posts,
        'contacts': contacts,
        'galleries': galleries,
        's_statics': sstatics,
        's_dynamics': sdynamics,
        'informations': informations,
        'socials': socials
    })
# Create your views here.
