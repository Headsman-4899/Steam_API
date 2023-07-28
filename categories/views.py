import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from categories.models import Category


def category_list(request):
    try:
        categories = Category.objects.all().values('id', 'title', 'main_category')
        return JsonResponse({'category_list': list(categories)})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def category_detail(request, id):
    try:
        category = get_object_or_404(Category, id=id)
        return JsonResponse({'category_detail': {'title': category.title,
                                                 'main_category_id': category.main_category}})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def category_create(request):
    try:
        if request.method == 'POST':
            body = json.loads(request.body.decode('UTF-8'))

            title = body.get('title')
            main_category_id = body.get('main_category_id')

            category = Category(title=title, main_category_id=main_category_id)

            category.save()
            return JsonResponse({'category_create': category.title})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def category_update(request, id):
    try:
        category = get_object_or_404(Category, id=id)
        if request.method == 'PUT':
            body = json.loads(request.body.decode('UTF-8'))

            title = body.get('title')
            main_category_id = body.get('main_category_id')

            category.title = title
            category.main_category_id = main_category_id

            category.save()
            return JsonResponse({'category_update': category.title})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def category_delete(request, id):
    try:
        category = get_object_or_404(Category, id=id)
        category.delete()
        return JsonResponse({'category_delete': category.title})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})
