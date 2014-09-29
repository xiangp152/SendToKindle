# coding=utf-8
# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from mysite import settings
from send_mail import *


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
    # media 不存在创建
    media_path = os.path.abspath(settings.MEDIA_ROOT)
    if not os.path.exists(media_path):
        os.makedirs()

    # 文件已存在则删除
    file_path = os.path.join(media_path, f.name)
    if os.path.exists(file_path):
        os.remove(file_path)
    destination = open(file_path, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    # if is_mobi(file_path):
    send_mail(file_path)
    # os.remove(file_path)

