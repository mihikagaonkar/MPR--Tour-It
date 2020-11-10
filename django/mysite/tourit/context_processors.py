from tourit.models import PlaceType

def sidenav(request):
    return{'sn':PlaceType.objects.all()}
