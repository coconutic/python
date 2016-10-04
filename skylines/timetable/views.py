from django.shortcuts import render, redirect
from django.http import HttpResponse
from forms import UserLogInForm, UserSignInForm
from . import db_manager




def shedule(request):
    return HttpResponse('do')

def log_in(request):
    if request.method == 'POST':
        form = UserLogInForm(request.POST)

        if (form.is_valid()):
            return redirect('/timetable/home')
    else:
        form = UserLogInForm()

    return render(request, 'timetable/log_in.html', {'form': form})

def sign_in(request):
    if request.method == 'POST':
        form = UserSignInForm(request.POST)

        if (form.is_valid()):
            register_user(form)
            return redirect('/timetable/main')
    else:
        form = UserSignInForm()

    return render(request, 'timetable/sign_in.html', {'form': form})


def main(request):
    request_type = request.GET.get('sing_in')
    print request_type
    return render(request, 'timetable/temp.html')
