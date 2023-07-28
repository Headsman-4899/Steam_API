import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from system_requirements.models import SystemRequirement


# Create your views here.
def system_requirements_list(request):
    try:
        system_requirements = SystemRequirement.objects.all().values('id',
                                                                     'os',
                                                                     'processor',
                                                                     'ram',
                                                                     'video_card',
                                                                     'direct_x',
                                                                     'disk_space')
        return JsonResponse({'system_requirements_list': list(system_requirements)})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def system_requirements_detail(request, id):
    try:
        system_requirements = SystemRequirement.objects.filter(id=id).values('id',
                                                                             'os',
                                                                             'processor',
                                                                             'ram',
                                                                             'video_card',
                                                                             'direct_x',
                                                                             'disk_space').first()
        if system_requirements:
            return JsonResponse({'system_requirements_detail': system_requirements})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def system_requirements_create(request):
    try:
        if request.method == 'POST':
            body = json.loads(request.body.decode('UTF-8'))

            os = body.get('os')
            processor = body.get('processor')
            ram = body.get('ram')
            video_card = body.get('video_card')
            direct_x = body.get('direct_x')
            disk_space = body.get('disk_space')

            system_requirements = SystemRequirement.objects.create(os=os,
                                                                   processor=processor,
                                                                   ram=ram,
                                                                   video_card=video_card,
                                                                   direct_x=direct_x,
                                                                   disk_space=disk_space)
            system_requirements.save()
            return JsonResponse({'system_requirements_create': {'id': system_requirements.id,
                                                                'os': system_requirements.os,
                                                                'processor': system_requirements.processor,
                                                                'ram': system_requirements.ram,
                                                                'video_card': system_requirements.video_card,
                                                                'direct_x': system_requirements.direct_x,
                                                                'disk_space': system_requirements.disk_space}})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def system_requirements_update(request, id):
    try:
        system_requirements = get_object_or_404(SystemRequirement, id=id)
        if request.method == 'PUT':
            body = json.loads(request.body.decode('UTF-8'))

            os = body.get('os')
            processor = body.get('processor')
            ram = body.get('ram')
            video_card = body.get('video_card')
            direct_x = body.get('direct_x')
            disk_space = body.get('disk_space')

            system_requirements.os = os
            system_requirements.processor = processor
            system_requirements.ram = ram
            system_requirements.video_card = video_card
            system_requirements.direct_x = direct_x
            system_requirements.disk_space = disk_space

            system_requirements.save()
            return JsonResponse({'system_requirements_update': {'id': str(system_requirements.id),
                                                                'os': system_requirements.os,
                                                                'processor': system_requirements.processor,
                                                                'ram': system_requirements.ram,
                                                                'video_card': system_requirements.video_card,
                                                                'direct_x': system_requirements.direct_x,
                                                                'disk_space': system_requirements.disk_space}})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})


def system_requirements_delete(request, id):
    try:
        system_requirements = get_object_or_404(id=id)
        system_requirements.delete()
        return JsonResponse({'system_requirements_delete': f'system requirements with id: {system_requirements.id} deleted successfully'})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'Error': error_message})
