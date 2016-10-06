from django.shortcuts import render, redirect
from django.http import HttpResponse
from forms import UserLogInForm, UserSignInForm
from . import db_manager
import json

cur_email = 'kattekurach@gmail.com'


def shedule(request):
    return HttpResponse('do')


def log_in(request):
    if request.method == 'POST':
        form = UserLogInForm(request.POST)
        if (form.is_valid()):
            if (db_manager.check_user(form['email'].value(), form['password'].value())):
                cur_email = form['email'].value()
                return redirect('/timetable/main')
            else:
                return redirect('/timetable/main/sign_in')
    else:
        form = UserLogInForm()
    return render(request, 'timetable/log_in.html', {'form': form})


def sign_in(request):
    if request.method == 'POST':
        form = UserSignInForm(request.POST)
        if (form.is_valid()):
            db_manager.add_user(form['username'].value(), form['email'].value(), form['password'].value())
            return redirect('/timetable/main')
    else:
        form = UserSignInForm()
    return render(request, 'timetable/sign_in.html', {'form': form})


def see_users(request):
    if request.method == 'GET':
        request_type = request.GET.get('request_type')
        if (request_type == "delete_user"):
            array_of_users = json.loads(request.GET.get('user_mails'))
            for mail in array_of_users:
                db_manager.remove_user(mail)
            return HttpResponse('success')
    list_users = db_manager.get_list_users()
    context = {'users_list' : list_users}

    return render(request, 'timetable/table_users.html', context)


def see_planes(request):
    if request.method == 'GET':
        request_type = request.GET.get('request_type')
        if request_type == "delete_planes":
            plane_cost = request.GET.get('plane_cost')            
            array_of_planes = json.loads(request.GET.get('plane_cost'))

            for plane in array_of_planes:
                print plane[0], plane[1], plane[2]
                print type(plane[0]), type(plane[1]), type(plane[2])
                db_manager.remove_plane(plane[0], plane[1], plane[2])

            return HttpResponse('success')
        elif request_type == 'add_plane':
            cost = request.GET.get('plane_cost')
            seats = request.GET.get('plane_seats')
            
            try:
                cost = int(cost)
                seats = int(seats)
            except:
                return HttpResponse('Cost and seats should be integer type.')

            db_manager.add_airplane(cost, seats, seats)
            return HttpResponse('success')

    list_planes = db_manager.get_list_airplanes()
    context = {'planes_list' : list_planes}
    return render(request, 'timetable/table_planes.html', context)


def see_history(request):
    list_history = db_manager.get_list_history(cur_email)
    context = {'history_list' : list_history}
    return render(request, 'timetable/table_history.html', context)


def main(request):
    request_type = request.GET.get('sing_in')
    print request_type
    return render(request, 'timetable/temp.html')
