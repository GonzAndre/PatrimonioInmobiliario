from django import template
from propiedades2.models import Notification
import datetime
from django.utils import timezone

register = template.Library()

@register.simple_tag
def tag_notification(request):
    objetos = Notification.objects.filter(user_receiver__username_staff = request.user).order_by('-time')
    for noti in objetos:
        delta = timezone.now()-noti.time
        if delta.days != 0:
            Notification.objects.filter(pk = noti.pk).update(time_str = (str(delta.days)+' d'))
        else:
            aux = str(delta).split(':')
            if aux[0] != '0':
                Notification.objects.filter(pk = noti.pk).update(time_str=(aux[0]+' h'))
            else:
                if aux[1][0] != '0':
                    Notification.objects.filter(pk = noti.pk).update(time_str=(aux[1]+' m'))
                else:
                    Notification.objects.filter(pk = noti.pk).update(time_str=(aux[1][1]+' m'))
    return Notification.objects.filter(user_receiver__username_staff = request.user).order_by('-time')
