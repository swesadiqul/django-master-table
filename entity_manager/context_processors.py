from .models import Type


def types(request):
    types = Type.objects.all()
    return {'types': types}