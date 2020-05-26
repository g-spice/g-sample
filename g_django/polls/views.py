from django.shortcuts import render
from datetime import datetime

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    d = {
        'hour': datetime.now().hour,
        'message': 'Sample message',
    }
    
    return render(request, 'polls/index.html')
