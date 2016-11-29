from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Choice
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings


@login_required(login_url="login/")
def index(request):
    choice_list = Choice.objects.order_by('position')
    context = {'choice_list': choice_list}
    return render(request, 'index.html', context)

@login_required(login_url="/login/")
def select(request, choice_id):
    selected=Choice.objects.filter(id=choice_id)
    import RPi.GPIO as GPIO
    import time
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(settings.DIRECTION_PIN, GPIO.OUT)
    GPIO.setup(settings.STEP_PIN, GPIO.OUT)
    GPIO.output( settings.DIRECTION_PIN, GPIO.HIGH)
    GPIO.output( settings.STEP_PIN, GPIO.LOW)
    for i in range (0,80):
        GPIO.output( settings.STEP_PIN, GPIO.HIGH)
        time.sleep(0.01)
        GPIO.output( settings.STEP_PIN, GPIO.LOW)

    GPIO.output( settings.DIRECTION_PIN, GPIO.LOW)
    for i in range (0,selected[0].position):
        GPIO.output( settings.STEP_PIN, GPIO.HIGH)
        time.sleep(0.01)
        GPIO.output( settings.STEP_PIN, GPIO.LOW)

    context = {'choice': selected[0].choice_text}
    return render(request, 'select.html', context)
