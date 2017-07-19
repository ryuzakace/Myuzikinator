from django.views import generic

from django.views.generic.edit import CreateView
from .models import Album

class IndexView(generic.ListView):
	template_name = 'music/index.html'
	context_object_name = 'all_albums'

	def get_queryset(self):
		return Album.objects.all()

class DetailView(generic.DetailView):
	model = Album
	template_name = 'music/detail.html'

class AlbumCreate(CreateView):
	model = Album
	fields=['artist', 'album_title','genre', 'album_logo']

class Logout(generic.ListView):
	model=Album
	template_name = 'music/logout.html'

class AboutView(generic.ListView):
	model=Album
	template_name = 'music/about.html'

