from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.models import User
#from .models import Tag
from .models import Question
from .forms import QuestionForm 
from django.db.models import Q


"""
Import other models as needed from .models and .forms or they won't work!
"""
# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return redirect (to='my_qbox')

    return render(request, "qbox/home.html")

def my_qbox(request):
    questions = request.user.questions.all()
    answers = request.user.answers.all
    return render(request, "qbox/my_qbox.html", {"questions": questions, "answers": answers})

def create_question(request):
    if request.method == "POST":
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            #question.set_tag_names(form.cleaned_data['tag_names'])
            return redirect(to='my_qbox')
    else:
        form = QuestionForm()

    return render(request, "qbox/create_question.html", {"form": form})