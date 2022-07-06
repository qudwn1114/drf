from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpRequest, JsonResponse
from config.task import process

# Create your views here.
class IndexView(TemplateView):
    '''
    메인 화면
    김병주/2022.07.13
    '''
    template_name = 'index.html'
    def get(self, request: HttpRequest, *args, **kwargs):
        context = {}

        return render(request, self.template_name, context)

    def post(self, request: HttpRequest, *args, **kwargs):
        context = {}
        task = process.delay(1)
        
        context['task_id'] = task.task_id
        
        context['message'] = f'task dispatched...'


        return render(request, self.template_name, context)