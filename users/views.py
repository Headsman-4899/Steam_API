import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone

from users.models import User


def user_list(request):
    users = User.objects.all().values('id', 'username', 'first_name', 'last_name',
                                      'email', 'balance', 'created_date', 'modified_date', 'is_active',
                                      'is_invisible', 'last_time_online', 'country_id', 'last_login', 'is_superuser', 'is_staff', 'date_joined')
    try:
        return JsonResponse({'user_list': list(users)})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def user_detail(request, id):
    try:
        user = get_object_or_404(User, id=id)
        user_data = {
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'balance': user.balance,
            'is_active': user.is_active,
            'is_invisible': user.is_invisible,
            'country_id': user.country_id
        }
        return JsonResponse({'user_detail': user_data})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def user_create(request):
    try:
        if request.method == 'POST':
            body = json.loads(request.body.decode('UTF-8'))

            username = body.get('username')
            first_name = body.get('first_name')
            last_name = body.get('last_name')
            email = body.get('email')
            password = body.get('password')
            balance = body.get('balance')
            country_id = body.get('country_id')

            user = User(username=username,
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        password=password,
                        balance=balance,
                        created_date=timezone.now(),
                        modified_date=timezone.now(),
                        is_active=True,
                        is_invisible=False,
                        last_time_online=timezone.now(),
                        country_id=country_id)

            user.save()
            return JsonResponse({'user_create': user.username})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def user_update(request, id):
    try:
        user = get_object_or_404(User, id=id)
        if request.method == 'PUT':
            body = json.loads(request.body.decode('UTF-8'))

            username = body.get('username')
            first_name = body.get('first_name')
            last_name = body.get('last_name')
            email = body.get('email')
            balance = body.get('balance')
            is_active = body.get('is_active')
            is_invisible = body.get('is_invisible')
            country_id = body.get('country_id')

            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.balance = balance
            user.is_active = is_active
            user.is_invisible = is_invisible
            user.country_id = country_id

            user.save()
            user_data = {
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'balance': user.balance,
                'is_active': user.is_active,
                'is_invisible': user.is_invisible,
                'country_id': user.country_id
            }
            return JsonResponse({'user_update': user_data})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def user_delete(request, id):
    try:
        user = get_object_or_404(User, id=id)
        user.delete()
        return JsonResponse({'user_delete': f'User {user.username} deleted successfully'})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})
