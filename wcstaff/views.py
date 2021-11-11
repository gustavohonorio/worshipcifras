from django.shortcuts import render


def staff(request):
    return render(request, 'staff.html')

