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
    # from zeep import Client

    # 'host' = > 'https://status-m.com.ua/ws/',
    # 'login' = > 'wser',
    # 'password' = > 'a1s2d3f4g5h6'

    # client = Client('http://www.webservicex.net/ConvertSpeed.asmx?WSDL')
    # result = client.service.ConvertSpeed(
    #     100, 'kilometersPerhour', 'milesPerhour')
    #
    # assert result == 62.137

    import zeep


    wsdl = 'https://status-m.com.ua/ws/ProductSearch_new.1cws?wsdl'
    product_search = Ws1c(wsdl, 'wser', 'a1s2d3f4g5h6')
    response = product_search.client.service.SearchClient(query=code)
    aaa = product_search.to_object(response)['data']

    select = request.POST['name_field']
    latest_question_list = TablePsPrice1C.objects.filter(
            article__icontains=select
        )
    context = {'latest_question_list': latest_question_list}
    return render(request, 'status/index.html', context)




