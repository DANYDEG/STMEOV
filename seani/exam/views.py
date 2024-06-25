import random
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CandidateForm
from django.contrib.auth.models import User

from.models import Breakdown, Exam
from django.contrib.auth.decorators  import login_required

# Create your views here.


@login_required
def home(request):
    user = request.user
    if user.is_superuser:
        return redirect('admin:index')
    return render(request, 'exam/home.html', {'user': user})

@login_required
def data(request):
    user = request.user
    return render(request, 'exam/userdata.html', {'user': user})

@login_required
def test(request, q_id=1):
    exam = request.user.exam

    # Obtener todas las preguntas de todos los módulos
    questions = list(Breakdown.objects.filter(exam=exam))

    # Barajar las preguntas si es la primera pregunta
    if q_id == 1:
        random.shuffle(questions)
        request.session['questions'] = [q.id for q in questions]

    # Obtener la pregunta actual
    questions_ids = request.session.get('questions')
    current_question = get_object_or_404(Breakdown, id=questions_ids[q_id - 1])

    if request.method == 'POST':
        answer = request.POST['answer']
        current_question.answer = answer
        current_question.save()

        if q_id < len(questions):
            return redirect('exam:test', q_id=q_id + 1)
        else:
            exam.compute_score()
            # Calcular la puntuación por módulo
            for module in exam.modules.all():
                exam.compute_score_by_module(module.id)
            return redirect('exam:results')

    return render(request, 'exam/test.html', {
        'question': current_question.question,
        'answer': current_question.answer,
        'q_id': q_id,
        'total_questions': len(questions),
    })

@login_required
def results(request):
    exam = request.user.exam
    modules = exam.exammodule_set.all().order_by('-score')
    return render(request, 'exam/results.html', {'modules': modules})



@login_required
def add_candidate(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            
            #recibir datos

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            career = form.cleaned_data['career']
            stage = form.cleaned_data['stage']

            #crear usuario
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()


            #crear examen
            exam = Exam.objects.create(
                user=user, 
                career=career, 
                stage=stage)
            
            exam.set_modules()
            exam.set_questions()
            return HttpResponse('Usuario y examen creado!')


            #llenar examen
        
        

    form = CandidateForm()
    return render(request, 'exam/add_candidate.html',
                  {'form': form})