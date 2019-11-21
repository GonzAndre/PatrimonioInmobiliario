def delete_notification(request):
    pk_noti = request.POST.get('id_notification')
    print(pk_noti)
    if request.POST.get('id_notification') != None:
        Notification.objects.filter(pk = pk_noti).delete()
        return JsonResponse({'result':True})
    else:
        return JsonResponse({'result':False})


def view_notificaction(request):
    data = {}
    data['Notifications'] = Notification.objects.filter(user_receiver__username_staff = request.user).order_by('-time')
    for noti in data['Notifications']:
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
    return render(request, 'notifications.html', data)

def create_notification(user, action, id_property, type_p):
    users = Staff.objects.all()
    for a in users:
        if a.username_staff != user:
            alert = Notification()
            alert.user_transmitter = Staff.objects.get(username_staff=user)
            alert.user_receiver = a
            alert.type_property = type_p
            alert.id_property = id_property
            alert.action = action
            if action == 'AA':
                alert.text = 'añadió una propiedad adquirida'
                string_2 = 'view_acquisition'
                alert.link = string_2
            if action == 'AR':
                alert.text = 'añadió una propiedad rentada'
                string_2 = 'view_rent'
                alert.link = string_2
            if action == 'EA':
                alert.text = 'modificó una propiedad adquirida'
                string_2 = 'view_acquisition'
                alert.link = string_2
            if action == 'ER':
                alert.text = 'modificó una propiedad rentada'
                string_2 = 'view_rent'
                alert.link = string_2
            if action == 'SA':
                alert.text = 'habilitó el estatus de una propiedad'
                if type_p == 'AC':
                    string_2 = 'view_acquisition'
                else:
                    string_2 = 'view_rent'
                alert.link = string_2
            if action == 'SI':
                alert.text = 'deshabilitó el estatus de una propiedad'
                if type_p == 'AC':
                    string_2 = 'view_acquisition'
                else:
                    string_2 = 'view_rent'
                alert.link = string_2
            if action == 'PA':
                alert.text = 'comentó en una propiedad adquirida'
                string_2 = 'view_acquisition'
                alert.link = string_2
            if action == 'PR':
                alert.text = 'comentó en una propiedad rentada'
                string_2 = 'view_rent'
                alert.link = string_2
            if action == 'RA':
                alert.text = 'respondió en una propiedad adquirida'
                string_2 = 'view_acquisition'
                alert.link = string_2
            if action == 'RR':
                alert.text = 'respondió en una propiedad rentada'
                string_2 = 'view_rent'
                alert.link = string_2
            alert.save()
    return True