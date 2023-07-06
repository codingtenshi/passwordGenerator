from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def password(request):
    length = request.POST.get('length')
    return render(request, 'password.html', {'length': length})
