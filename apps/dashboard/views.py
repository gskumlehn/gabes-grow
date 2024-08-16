from datetime import datetime

from django.shortcuts import render, redirect

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    collection_time = datetime.now().strftime("%H:%M")
    return render(request, 'dashboard/index.html', {"humidity": 67.2, "temperature": 23.4, "dry": True, "time": collection_time})
