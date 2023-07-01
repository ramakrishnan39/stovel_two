from django.shortcuts import render

# Create your views here.
def v_index(request):
  return render(request,'index.html')


def v_home(request):
  return render(request, "home.html")