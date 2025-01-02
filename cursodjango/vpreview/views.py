from django.shortcuts import render


def video(request, slug):
    videos = {
        'preview': {
            'titulo': 'Preview do Curso de Python e Django:',
            'vimeo_id': 1043031414,
            'vimeo_titulo': 'Python-preview-course'
        },
        'variaveis': {
            'titulo': 'Curso de Python e Django: Variáveis:',
            'vimeo_id': 1043327662,
            'vimeo_titulo': 'Variáveis-em-Python'
        }
    }

    video = videos[slug]

    return render(request, 'vpreview/video.html', context={'video': video})
