from django.shortcuts import render
from .forms import EmailForm

from django.http import HttpResponse
from django.http import Http404
from django.http import JsonResponse

from pyairtable import Table
from pyairtable.formulas import match
from django.conf import settings
import json 

mailing_list_base_id = 'appg0ZB5BdqDQHGAR'
sign_ups_table_name = 'Sign Ups'
at_mailing_list = Table(settings.AIRTABLE_API_KEY, mailing_list_base_id, sign_ups_table_name)

# Create your views here.

def index(request):
    #return render(request, 'main_portal/index.html', context)
    return HttpResponse("Hello, world.")

def get_profile(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EmailForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            email = form.cleaned_data['email']
            record = get_record_by_email(email)
            formatted_profile = format_profile(record['fields'])
            return render(request, 'main_portal/show_profile.html', {'profile_data': formatted_profile})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmailForm()

    return render(request, 'main_portal/get_profile.html', {'form': form})

# Endpoint for testing
def test_airtable(request):
    email = "kspatel2018@gmail.com"
    record = get_record_by_email(email)
    json_object = json.dumps(record, indent = 4) 
    print(json_object)
    return HttpResponse(json_object, content_type="application/json")

def format_profile(fields):
    return {
        "id": fields.get('ID'),
        "first_name": fields.get('First Name'), 
        "last_name": fields.get('Last Name'), 
        "email": fields.get('Email'),
        "linkedin": fields.get('LinkedIn'),
        "twitter": fields.get('Twitter'),
        "current_role": fields.get('Current Role'),
        "company": fields.get('Company'),
        "chapter": fields.get('Chapter'),
    }

def get_record_by_email(email):
    formula = match({"email": email})
    email_record = at_mailing_list.first(formula=formula)
    return email_record

# kishan_record_id = 'recmC5JlyE9MI56Vi'
# abhishek_record_id = 'rec3eU7NaGRr0TPmo'
def get_record_by_id(record_id):
    # fetched as python dict
    record = at_mailing_list.get(record_id)
    return record