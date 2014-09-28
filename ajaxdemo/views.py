# Create your views here.
import os

from django.shortcuts import render_to_response
from django.template import RequestContext
from mysite import settings


def handle_request(request):
    if request.method == "GET":
        return handle_get(request)
    elif request.method == "POST":
        return handle_post(request)


def handle_post(request):
    # handle file
    if 'file' in request.FILES:
        handle_uploaded_file(request.FILES['file'])


def handle_get(request):
    return render_to_response('index.html', {'STATIC_URL': settings.STATIC_URL, },
                              context_instance=RequestContext(request))


def handle_uploaded_file(f):
    file_path = os.path.join(os.path.abspath(settings.MEDIA_ROOT), f.name)
    destination = open(file_path, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    os.remove(file_path)


def send_mail():
    pass