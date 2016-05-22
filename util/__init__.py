__author__ = 'abcdroid'
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from pytz import timezone


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def get_object_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None


def get_local_date(fecha):
    time_zone = timezone("America/Lima")
    return fecha.astimezone(time_zone).strftime("%I:%M %p")