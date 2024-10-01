from django.shortcuts import render
from django.http import HttpResponse
from .models import services, Service

# Create your views here.
# def add(request):
#     return HttpResponse("Helloworld")


# def add(request):
#     return render(request, 'index.html')


def add(request):
    # s1 = services()
    # s1.title = 'Best gardening'
    # s1.des = "We provide best gardening services ever"
    # s1.img = 'pexels-photo-147640.jpeg'
    #
    # s2 = services()
    # s2.title = 'Best watering'
    # s2.des = "We provide best watering services ever"
    # s2.img = 'pexels-photo-4750274.jpeg'
    #
    # s3 = services()
    # s3.title = 'Best caring'
    # s3.des = "We provide best caring services ever"
    # s3.img = 'pexels-photo-212942.jpeg'
    #
    # sess = [s1, s2, s3]
    sess = Service.objects.all()

    return render(request, 'index.html', {'ses': sess})


def contact(request):
    return render(request, 'contact.html')


def blog_post_1(request):
    return render(request, 'blog-home-1.html')


def blog_post_2(request):
    return render(request, 'blog-home-2.html')


def blog_post_3(request):
    return render(request, 'blog-post.html')
