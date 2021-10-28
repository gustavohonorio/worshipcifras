from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages


def register(request):
    return render(request=request, template_name='register.html')
