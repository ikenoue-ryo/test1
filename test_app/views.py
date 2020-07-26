from django.shortcuts import render, redirect


def indexfunc(request):
    user = Question.objects.get(id=request.user.id)

    if request.method == 'POST':
        user.favorite_food = request.POST['favorite_food']
        user.save()

    return render(request, 'main_app/index.html')
