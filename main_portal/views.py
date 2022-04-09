from django.shortcuts import render

from django.http import HttpResponse
from django.http import Http404
from django.http import JsonResponse

from pyairtable import Table
from django.conf import settings
mailing_list_base_id = 'appg0ZB5BdqDQHGAR'
sign_ups_table_name = 'Sign Ups'
at_mailing_list = Table(settings.AIRTABLE_API_KEY, mailing_list_base_id, sign_ups_table_name)

# Create your views here.
# Endpoint for testing
def test_airtable(request):
    kishan_record_id = 'recmC5JlyE9MI56Vi'
    record = at_mailing_list.get(kishan_record_id)
    return HttpResponse(record,content_type="application/json")

    return JsonResponse(record)
    return HttpResponse('call made')