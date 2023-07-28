import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from publishers.models import Publisher


def publisher_list(request):
    try:
        publishers = Publisher.objects.all().values('id', 'name', 'rating')
        return JsonResponse({'publisher_list': list(publishers)})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def publisher_detail(request, id):
    try:
        publisher = Publisher.objects.filter(id=id).values('id', 'name', 'rating').first()
        if publisher:
            return JsonResponse({'publisher_detail': publisher})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def publisher_create(request):
    try:
        if request.method == 'POST':
            body = json.loads(request.body.decode('UTF-8'))

            name = body.get('name')
            rating = body.get('rating')

            publisher = Publisher.objects.create(name=name, rating=rating)

            publisher.save()
            return JsonResponse({'publisher_create': {'id': publisher.id,
                                                      'name': publisher.name,
                                                      'rating': publisher.rating}})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def publisher_update(request, id):
    try:
        publisher = get_object_or_404(Publisher, id=id)
        if request.method == 'PUT':
            body = json.loads(request.body.decode('UTF-8'))

            name = body.get('name')
            rating = body.get('rating')

            publisher.name = name
            publisher.rating = rating

            publisher.save()
            return JsonResponse({'publisher_update': {'id': str(publisher.id),
                                                      'name': publisher.name,
                                                      'rating': publisher.rating}})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def publisher_delete(request, id):
    try:
        publisher = get_object_or_404(Publisher, id=id)
        publisher.delete()
        return JsonResponse({'publisher_delete': f'Publisher {publisher.name} deleted successfully'})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})
