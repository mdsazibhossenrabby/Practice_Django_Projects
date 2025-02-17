from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def dynamic_page(request, page_slug):
    # You can fetch dynamic content from database using slug
    context = {'slug': page_slug}
    return render(request, 'dynamic_page.html', context)