import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from games.models import Game


def game_list(request):
    try:
        games = Game.objects.all().values('id', 'picture', 'title', 'description',
                                          'cost', 'age_rating', 'rating',
                                          'min_system_requirements_id',
                                          'rec_system_requirements_id',
                                          'developer_id', 'category_id')
        return JsonResponse({'games': list(games)})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def game_detail(request, id):
    try:
        game = Game.objects.filter(id=id).values('id', 'picture', 'title', 'description',
                                                 'cost', 'age_rating', 'rating',
                                                 'min_system_requirements_id',
                                                 'rec_system_requirements_id',
                                                 'developer_id', 'category_id').first()
        if game:
            return JsonResponse({'game_detail': game})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def game_create(request):
    try:
        if request.method == 'POST':
            body = json.loads(request.body.decode('UTF-8'))

            picture = body.get('picture')
            title = body.get('title')
            description = body.get('description')
            cost = body.get('cost')
            age_rating = body.get('age_rating')
            rating = body.get('rating')
            min_system_requirements_id = body.get('min_system_requirements_id')
            rec_system_requirements_id = body.get('rec_system_requirements_id')
            developer_id = body.get('developer_id')
            category_id = body.get('category_id')

            game = Game.objects.create(picture=picture, title=title, description=description,
                                       cost=cost, age_rating=age_rating, rating=rating,
                                       min_system_requirements_id=min_system_requirements_id,
                                       rec_system_requirements_id=rec_system_requirements_id,
                                       developer_id=developer_id, category_id=category_id)

            game.save()
            return JsonResponse({'game_create': game.title})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def game_update(request, id):
    try:
        game = get_object_or_404(Game, id=id)
        if request.method == 'PUT':
            body = json.loads(request.body.decode('UTF-8'))

            picture = body.get('picture')
            title = body.get('title')
            description = body.get('description')
            cost = body.get('cost')
            age_rating = body.get('age_rating')
            rating = body.get('rating')
            min_system_requirements_id = body.get('min_system_requirements_id')
            rec_system_requirements_id = body.get('rec_system_requirements_id')
            developer_id = body.get('developer_id')
            category_id = body.get('category_id')

            game.picture = picture
            game.title = title
            game.description = description
            game.cost = cost
            game.age_rating = age_rating
            game.rating = rating
            game.min_system_requirements_id = min_system_requirements_id
            game.rec_system_requirements_id = rec_system_requirements_id
            game.developer_id = developer_id
            game.category_id = category_id

            game.save()
            return JsonResponse({'game_update': game.title})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def game_delete(request, id):
    try:
        game = get_object_or_404(Game, id=id)
        game.delete()
        return JsonResponse({'game_delete': game.title})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})

