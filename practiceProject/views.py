from django.http import HttpResponse
from django.shortcuts import render
def home(request):
  # return HttpResponse("Hello, world! You are at Home of the webpage")
  return render(request, 'website/index.html')

def about(request):
  # return HttpResponse("Hello, world! You are at About webpage")
  return render(request, 'website/about.html')

def contact(request):
  # return HttpResponse("Hello, world! You are at Contacts webpage")
  return render(request, 'website/contact.html')