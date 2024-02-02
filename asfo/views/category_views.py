from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

def item(request):
    # question_list = Question.objects.order_by('-create_date')
    context = {'question_list': ''}
    return render(request, 'asfo/item.html', context)
