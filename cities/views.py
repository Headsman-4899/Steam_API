import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from cities.models import City
from countries.models import Country


def city_list(request):
    try:
        cities = City.objects.all().values('id', 'name', 'country_id')
        return JsonResponse({'city_list': list(cities)})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def city_detail(request, id):
    try:
        city = get_object_or_404(City, id=id)
        return JsonResponse({'city_detail': {'name': city.name}})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def city_create(request):
    try:
        if request.method == 'POST':
            body = json.loads(request.body.decode('UTF-8'))
            name = body.get('name')
            country_id = body.get('country_id')

            new_city = City(name=name, country_id=country_id)

            new_city.save()
            return JsonResponse({'city_create': {'id': new_city.name}})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def city_update(request, id):
    try:
        updated_city = get_object_or_404(City, id=id)
        if request.method == 'PUT':
            body = json.loads(request.body.decode('UTF-8'))
            name = body.get('name')
            country_id = body.get('country_id')

            updated_city.name = name
            if country_id:
                country = Country.objects.get(id=country_id)
                updated_city.country = country

            updated_city.save()
            return JsonResponse({'city_update': {'name': updated_city.name}})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def city_delete(request, id):
    try:
        city = get_object_or_404(City, id=id)
        city.delete()
        return JsonResponse({'city_delete': f'city {city.name} deleted successfully'})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})
