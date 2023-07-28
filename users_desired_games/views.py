import json

from games.models import Game
from users.models import User
from django.http import JsonResponse

from .models import UserDesiredGames


# Create your views here.
def user_desired_games_list(request):
    try:
        user_desired_games = UserDesiredGames.objects.all().values('id',
                                                                   'added_date',
                                                                   'user_id',
                                                                   'game_id')
        return JsonResponse({'user_desired_games_list': list(user_desired_games)})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def user_desired_games_detail(request, id):
    try:
        user_desired_game = UserDesiredGames.objects.get(id=id)
        user_desired_game_data = {
            'id': user_desired_game.id,
            'added_date': user_desired_game.added_date,
            'user_id': user_desired_game.user_id,
            'game_id': user_desired_game.game_id
        }
        return JsonResponse({'user_desired_game_detail': user_desired_game_data})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def user_desired_games_create(request):
    try:
        if request.method == 'POST':
            body = json.loads(request.body.decode('UTF-8'))
            user_id = body.get('user_id')
            game_id = body.get('game_id')

            user = User.objects.get(id=user_id)
            game = Game.objects.get(id=game_id)

            user_desired_game = UserDesiredGames(user=user, game=game)

            user_desired_game.save()
            user_desired_game_data = {
                'id': user_desired_game.id,
                'added_date': user_desired_game.added_date,
                'user_id': user_desired_game.user_id,
                'game_id': user_desired_game.game_id
            }
            return JsonResponse({'user_desired_game_create': user_desired_game_data})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def user_desired_games_update(request, id):
    try:
        if request.method == 'PUT':
            user_desired_game = UserDesiredGames.objects.get(id=id)
            body = json.loads(request.body.decode('UTF-8'))

            user_id = body.get('user_id')
            game_id = body.get('game_id')

            if user_id:
                user = User.objects.get(id=user_id)
                user_desired_game.user = user
            if game_id:
                game = Game.objects.get(id=game_id)
                user_desired_game.game = game

            user_desired_game.save()
            user_desired_game_data = {
                'id': user_desired_game.id,
                'added_date': user_desired_game.added_date,
                'user_id': user_desired_game.user_id,
                'game_id': user_desired_game.game_id
            }
            return JsonResponse({'user_desired_game_update': user_desired_game_data})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def user_desired_games_delete(request, id):
    try:
        user_desired_game = UserDesiredGames.objects.get(id=id)
        user_desired_game.delete()
        return JsonResponse({'user_desired_game_delete': 'User`s desired game deleted successfully.'})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})
