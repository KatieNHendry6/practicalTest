from django.shortcuts import render
from main.models import page
#from django.http import HttpResponse

def index(request):
    # category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {}
    context_dict['pagelist'] = page.objects.order_by('-date')
    return render(request, 'main/index.html', context=context_dict)