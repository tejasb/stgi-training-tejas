from django.shortcuts import render

# Create your views here.

def landing_page(request):
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog/all-posts.html")

def single_post(request, slug):
    return render(request, f"blog/includes/post-{slug}.html")

