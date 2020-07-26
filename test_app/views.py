from django.shortcuts import render, redirect


def indexfunc(request):

    return render(request, 'test_app/index.html')
