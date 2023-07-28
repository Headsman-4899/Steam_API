import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from countries.models import Country


def country_list(request):
    try:
        countries = Country.objects.all().values('id', 'name')
        return JsonResponse({'country_list': list(countries)})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def country_detail(request, id):
    try:
        country = Country.objects.filter(id=id).values('id', 'name').first()
        return JsonResponse({'country_detail': country})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def country_create(request):
    try:
        if request.method == 'POST':
            body = json.loads(request.body.decode('UTF-8'))
            name = body.get('name')
            new_country = Country(name=name)
            new_country.save()
            return JsonResponse({'country_create': {'id': new_country.id,
                                                    'name': new_country.name}})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def country_update(request, id):
    try:
        country = get_object_or_404(Country, id=id)
        if request.method == 'PUT':
            body = json.loads(request.body.decode('UTF-8'))
            name = body.get('name')
            country.name = name
            country.save()
            return JsonResponse({'country_update': {'id': country.id,
                                                    'name': country.name}})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def country_delete(request, id):
    try:
        country = get_object_or_404(Country, id=id)
        country.delete()
        return JsonResponse({'country_delete': f'country {country.name} deleted successfully.'})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})
