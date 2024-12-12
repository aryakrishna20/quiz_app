
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Question
import random
# Create your views here.
def start_quiz(request):
    request.session['answered_questions'] = []
    request.session['correct_answers'] = 0
    request.session['total_questions'] = 0
    return redirect('get_question')

def get_question(request):
    answered_questions = request.session.get('answered_questions', [])
    unanswered_questions = Question.objects.exclude(id__in=answered_questions)
    if not unanswered_questions.exists():
        return redirect('results')
    
    question = random.choice(unanswered_questions)
    context = {'question': question}
    return render(request, 'quiz/index.html', context)

def submit_answer(request):
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        selected_option = request.POST.get('option')

        question = Question.objects.get(id=question_id)
        request.session['total_questions'] += 1
        if question.correct_option == selected_option:
            request.session['correct_answers'] += 1

        answered_questions = request.session.get('answered_questions', [])
        answered_questions.append(question_id)
        request.session['answered_questions'] = answered_questions

    return redirect('get_question')

def results(request):
    correct_answers = request.session.get('correct_answers', 0)
    total_questions = request.session.get('total_questions', 0)
    incorrect_answers = total_questions - correct_answers
    context = {
        'correct_answers': correct_answers,
        'total_questions': total_questions,
        'incorrect_answers': incorrect_answers,
    }
    return render(request, 'quiz/results.html', context)
