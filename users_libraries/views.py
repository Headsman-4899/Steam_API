import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from games.models import Game
from users.models import User
from users_libraries.models import UserLibrary


def user_library_list(request):
    try:
        user_library = UserLibrary.objects.all().values('id',
                                                        'total_time',
                                                        'is_favorite',
                                                        'user_id',
                                                        'game_id')
        return JsonResponse({'user_library_list': list(user_library)})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def user_library_detail(request, id):
    try:
        user_library = get_object_or_404(UserLibrary, id=id)
        return JsonResponse({'user_library_detail': {'id': user_library.id,
                                                     'total_time': user_library.total_time,
                                                     'is_favorite': user_library.is_favorite,
                                                     'user_id': user_library.user_id,
                                                     'game_id': user_library.game_id}})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def user_library_create(request):
    try:
        if request.method == 'POST':
            body = json.loads(request.body.decode('UTF-8'))

            is_favorite = body.get('is_favorite')
            user_id = body.get('user_id')
            game_id = body.get('game_id')
            user = User.objects.get(id=user_id)
            game = Game.objects.get(id=game_id)

            user_library = UserLibrary(is_favorite=is_favorite,
                                       user=user,
                                       game=game)

            user_library.save()
            return JsonResponse({'user_library_create': user_library.id})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def user_library_update(request, id):
    try:
        if request.method == 'PUT':
            user_library = UserLibrary.objects.get(id=id)
            body = json.loads(request.body.decode('UTF-8'))

            total_time = body.get('total_time')
            is_favorite = body.get('is_favorite')
            user_id = body.get('user_id')
            game_id = body.get('game_id')

            user_library.total_time = total_time
            user_library.is_favorite = is_favorite

            if user_id:
                user = User.objects.get(id=user_id)
                user_library.user = user

            if game_id:
                game = Game.objects.get(id=game_id)
                user_library.game = game

            user_library.save()
            return JsonResponse({'user_library_update': user_library.id})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def user_library_delete(request, id):
    try:
        user_library = UserLibrary.objects.get(id=id)
        user_library.delete()
        return JsonResponse({'user_library_delete': 'User library deleted successfully.'})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})
