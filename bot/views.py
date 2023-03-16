from django.shortcuts import render
from django.http import HttpResponse
from .forms import QuestionForm
from .forms import AnswerForm
import openai
# Create your views here.

def index(request):
    return render(request, "bot/index.html")


def Save_Question(request):
    if request.method == "POST":
        s = QuestionForm(request.POST)
        if s.is_valid():
            s.save()
            return HttpResponse('Successfully')
        else:
            return HttpResponse('404 NOT FOUND')
    else:
        return HttpResponse('404 NOT FOUND')



def Save_APIChatGPT(request):

    model = "code-davinci-002"  # "text-davinci-003"
    openai.api_key = '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'

    s = QuestionForm()
    question_text = "tôi bị ốm thì phải làm sao" #s.fields['question_text'].value
    response = openai.Completion.create(engine=model, temperature=1, prompt=question_text, max_tokens=256, n=1)
    answer_text = response.choices[0].text
    print(answer_text)
    return HttpResponse(answer_text, content_type="text/plain")
"""    q = AnswerForm()
    q.fields['answer_text'].value = answer_text
    if q.is_valid():
        q.save()
        return HttpResponse('Successfully')
    else:
        return HttpResponse('404 NOT FOUND')"""
