from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from status.models import TablePsPrice1C

class IndexView(generic.ListView):
    template_name = 'status/index.html'
    context_object_name = 'latest_question_list'
    select='BOSCH'

    def get_queryset(self):
         return TablePsPrice1C.objects.filter(
            brand_clean=self.select
        )#.order_by('-pub_date')[:5]

def msearch(request):
    select = request.POST['name_field']
    latest_question_list = TablePsPrice1C.objects.filter(
            article__contains=select
        )
    context = {'latest_question_list': latest_question_list}
    return render(request, 'status/index.html', context)




