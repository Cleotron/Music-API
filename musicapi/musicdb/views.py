from django.shortcuts import render
from .models import Artist

# Create your views here.

def artist_list(request):
    artists = Artist.objects.order_by('artist_name')
    return render(request, 'musicdb/artist_list.html', {'artists':artists})