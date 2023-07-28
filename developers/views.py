import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from developers.models import Developer


def developer_list(request):
    try:
        developers = Developer.objects.all().values('id', 'title', 'publisher_id')
        return JsonResponse({'developer_list': list(developers)})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def developer_detail(request, id):
    try:
        developer = Developer.objects.filter(id=id).values('id', 'title', 'publisher_id').first()
        if developer:
            return JsonResponse({'developer_detail': developer})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def developer_create(request):
    try:
        if request.method == 'POST':
            body = json.loads(request.body.decode('UTF-8'))

            title = body.get('title')
            publisher_id = body.get('publisher_id')

            developer = Developer.objects.create(title=title, publisher_id=publisher_id)

            developer.save()
            return JsonResponse({'developer_create': developer.title})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def developer_update(request, id):
    try:
        developer = get_object_or_404(Developer, id=id)
        if request.method == 'PUT':
            body = json.loads(request.body.decode('UTF-8'))

            title = body.get('title')
            publisher_id = body.get('publisher_id')

            developer.title = title
            developer.publisher_id = publisher_id

            developer.save()
            return JsonResponse({'developer_update': developer.title})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def developer_delete(request, id):
    try:
        developer = get_object_or_404(Developer, id=id)
        developer.delete()
        return JsonResponse({'developer_delete': {f'developer {developer.title} deleted successfully.'}})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})
