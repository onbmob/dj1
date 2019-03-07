from django.shortcuts import render
from django.views import generic

from status.models import TablePsPrice1C


class IndexView(generic.ListView):
    # template_name = 'status/index.html'
    # context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5]
        return TablePsPrice1C.objects


        # Return the last five published questions (not including those set to be
        # published in the future).

        # return TablePsPrice1C.objects.filter(
        #     pub_date__lte=timezone.now()
        # ).order_by('-pub_date')[:5]

