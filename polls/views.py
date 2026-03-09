from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Question, Choice

# Твої старі функції index та detail залишаються без змін
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:10]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

# --- НОВИЙ КОД ДОДАЄМО СЮДИ ---

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # Шукаємо варіант відповіді, який вибрав користувач
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Якщо користувач нічого не вибрав і натиснув кнопку
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Ви не обрали варіант відповіді.",
        })
    else:
        # Додаємо +1 голос і зберігаємо в базу даних
        selected_choice.votes += 1
        selected_choice.save()
        # Після успішного голосування перенаправляємо на сторінку результатів
        return HttpResponseRedirect(f"/{question.id}/results/")

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # Поки що просто повертаємо шаблон результатів (ми його створимо наступним кроком)
    return render(request, 'polls/results.html', {'question': question})