from django.shortcuts import render

from .models import Photo

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import redirect

# Create your views here.

def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos': photos})

class PhotoUploadView(CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'

    def form_vaild(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_vaild():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form': form})

class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'

class PhotoUpdateView(UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'
