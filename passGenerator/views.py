from django.shortcuts import render
import random
import string

# Create your views here.
# form
def generate_password(length, bigLetters=False, numbers=False, specials=False):
    characters = string.ascii_lowercase # zbiór małych liter
    if bigLetters:
        characters += string.ascii_uppercase # dodawanie dużych liter
    if numbers:
        characters += string.digits # dodawanie liczb
    if specials:
        characters += string.punctuation # dodawanie znaków specjalnych
    password = ''
    for _ in range(length):
        password += random.choice(characters)

    return password


def home(request):
    return render(request, 'home.html')

def password(request):
    length = request.POST.get('length')
    return render(request, 'password.html', {'length': length})
    length = int(request.POST.get('length'))
    big_letters_included = request.POST.get('big')
    numbers_included = request.POST.get('numbers')
    specials_included = request.POST.get('specials')
    password = generate_password(
        length, big_letters_included, specials_inclided)
    return render(request, 'password.html', {'password': password})
