from django.shortcuts import render
from .forms import UserProfileInfoForm

def index(request):
    if request.method == "POST":
        user_form = UserProfileInfoForm(request.POST,request.FILES)
        if user_form.is_valid():
            user_form.save()
        else:
            print(user_form.errors)
    else:
        user_form = UserProfileInfoForm()

    return render(request, 'form.html',
                  {"user_form": user_form})

