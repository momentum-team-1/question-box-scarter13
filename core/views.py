from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.models import User
from django.db.models import Q

"""
Import other models as needed from .models and .forms or they won't work!
"""
# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return redirect (to='my_questionbox')

    return render(request, "questionbox/home.html")

"""
Regarding the homepage view above: once you select the view to which you will redirect, you can bump the following line out to be in line with the if statement
"""

def my_questionbox(request):
    questions = request.user.questions.all()
    #answers = request.user.answers.all
    return render(request, "questionbox/my_questionbox.html", {"questions": questions})