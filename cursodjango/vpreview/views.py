from django.urls import reverse
from django.shortcuts import render


class Video:
    def __init__(self, slug, titulo, vimeo_id, vimeo_titulo):
        self.slug = slug
        self.titulo = titulo
        self.vimeo_id = vimeo_id
        self.vimeo_titulo = vimeo_titulo

    def get_absolute_url(self):
        return reverse('vpreview:video', args=(self.slug,))


videos = [
        Video(
            'preview',
            'Preview do Curso de Python e Django:',
            1043031414,
            'Python-preview-course'
        ),
        Video(
            'variaveis',
            'Curso de Python e Django: Variáveis:',
            1043327662,
            'Variáveis-em-Python'
        )
    ]

videos_dct = {v.slug: v for v in videos}


def indice(request):

    return render(request, 'vpreview/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'vpreview/video.html', context={'video': video})


#  ESTRUTURA HARDCODE PARA EXTRAIR DICIONÁRIOS DE UMA LISTA DE DICIONÁRIOS:
# videos = [
#         {
#             'slug': 'preview',
#             'titulo': 'Preview do Curso de Python e Django:',
#             'vimeo_id': 1043031414,
#             'vimeo_titulo': 'Python-preview-course'
#         },
#         {
#             'slug': 'variaveis',
#             'titulo': 'Curso de Python e Django: Variáveis:',
#             'vimeo_id': 1043327662,
#             'vimeo_titulo': 'Variáveis-em-Python'
#         }
#     ]
#
# videos_dct = {dct['slug']: dct for dct in videos}


# ESTRUTURA HARDCODE:
# def video(request, slug):
#     videos = {
#         'preview': {
#             'slug': 'preview',
#             'titulo': 'Preview do Curso de Python e Django:',
#             'vimeo_id': 1043031414,
#             'vimeo_titulo': 'Python-preview-course'
#         },
#         'variaveis': {
#             'slug': 'variaveis',
#             'titulo': 'Curso de Python e Django: Variáveis:',
#             'vimeo_id': 1043327662,
#             'vimeo_titulo': 'Variáveis-em-Python'
#         }
#     }
#     video = videos[slug]
#     return render(request, 'vpreview/video.html', context={'video': video})
