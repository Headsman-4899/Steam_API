import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from games.models import Game
from users.models import User
from .models import Review


# Create your views here.
def review_list(request):
    try:
        reviews = Review.objects.all().values('id',
                                              'comment',
                                              'point',
                                              'created_date',
                                              'user_id',
                                              'game_id',)
        return JsonResponse({'review_list': list(reviews)})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def review_detail(request, id):
    try:
        review = get_object_or_404(Review, id=id)
        review_data = {'id': str(review.id),
                       'comment': review.comment,
                       'point': review.point,
                       'created_date': review.created_date,
                       'user_id': str(review.user_id),
                       'game_id': str(review.game_id)}
        return JsonResponse({'review_detail': review_data})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def review_create(request):
    try:
        if request.method == 'POST':
            body = json.loads(request.body.decode('UTF-8'))

            comment = body.get('comment')
            point = body.get('point')
            user_id = body.get('user_id')
            game_id = body.get('game_id')
            user = User.objects.get(id=user_id)
            game = Game.objects.get(id=game_id)

            review = Review(comment=comment, point=point, user=user, game=game)

            review.save()
            review_data = {'id': str(review.id),
                           'comment': review.comment,
                           'point': review.point,
                           'created_date': review.created_date,
                           'user_id': str(review.user_id),
                           'game_id': str(review.game_id)}
            return JsonResponse({'review_create': review_data})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def review_update(request, id):
    try:
        review = get_object_or_404(Review, id=id)
        if request.method == 'PUT':
            body = json.loads(request.body.decode('UTF-8'))

            comment = body.get('comment')
            point = body.get('point')
            user_id = body.get('user_id')
            game_id = body.get('game_id')

            user = User.objects.get(id=user_id)
            game = Game.objects.get(id=game_id)
            review.comment = comment
            review.point = point
            review.user = user
            review.game = game

            review.save()
            review_data = {'id': str(review.id),
                           'comment': review.comment,
                           'point': review.point,
                           'created_date': review.created_date,
                           'user_id': str(review.user_id),
                           'game_id': str(review.game_id)}
            return JsonResponse({'review_update': review_data})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def review_delete(request, id):
    try:
        review = Review.objects.get(id=id)
        review.delete()
        return JsonResponse({'review_delete': 'Review deleted successfully'})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})
