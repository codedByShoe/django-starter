from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST

def home(request):
  return render(request, 'core/home.html')

@require_POST
def echo(request):
    message = request.POST.get('message', '')
    return HttpResponse(f"Echo: {message}")
