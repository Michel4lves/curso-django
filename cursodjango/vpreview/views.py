from django.shortcuts import render


def video(request, slug):
    return render(request, 'vpreview/video.html')
