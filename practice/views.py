from django.shortcuts import render


# Create your views here.
def practice_step(request):
  return render(request, 'practice/practice_step.html')
