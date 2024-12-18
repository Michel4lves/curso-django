from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse('<html><body>CURSO DJANGO</html></body>', content_type='text/html')
