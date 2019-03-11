import zeep
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Transport
from zeep.cache import InMemoryCache

from status.lib_ws_1c import Ws1c
from status.models import TablePsPrice1C


class IndexView(generic.ListView):
    template_name = 'status/index.html'
    context_object_name = 'latest_question_list'
    select = 'BOSCH'

    def get_queryset(self):
        return TablePsPrice1C.objects.filter(
            brand_clean=self.select
        )  # .order_by('-pub_date')[:5]


def msearch(request):
    # params = '<param> <action>getFullProducts</action> <clientСode>00000206</clientСode> </param>'
    # wsdl = 'http://vbndetal.com.ua/ws/soapservice_2.1cws?wsdl'
    # HTTPBasicAuth( 'web', '1111')
    # response = client.service.Goods(param=params)

    select = request.POST['name_field']
    dbList = TablePsPrice1C.objects.filter(
        article__icontains=select
    )

    if dbList:
        codes = ""
        for item in dbList:
            codes+=item.id_product+';'

        wsdl = 'https://status-m.com.ua/ws/ProductSearch_new.1cws?wsdl'
        cache_ = InMemoryCache(timeout=900)
        session = Session()
        session.auth = HTTPBasicAuth('wser', 'a1s2d3f4g5h6')
        client = zeep.Client(wsdl=wsdl, transport=Transport(session=session, cache=cache_))
        # with client.settings(raw_response=True, xml_huge_tree=True):
        with client.settings(strict=False):
            response = client.service.SearchByCodes(ClientCode="1454",
                                                    Codes=codes,
                                                    ShowOff="1",
                                                    ShowNumber="5000",
                                                    Sort="0",
                                                    Letter="",
                                                    ShowOrderGoods="",
                                                    Only_GAZ_Products="0")
        # print('response')
        # print(response)

        for item in response.TotalSearchResults.ElSearchResults:
            for dbitem in dbList:
                if dbitem.id_product == item.Code:
                    dbitem.price = item.Price
                    dbitem.balance = item.Balance
                    break


    context = {'latest_question_list': dbList}

    return render(request, 'status/index.html', context)
