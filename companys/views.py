from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from companys.models import Companys, Pay
from .models import *
# from tagging.models import Tag, TaggedItem
# from tagging.views import TaggedObjectList

from django.views.generic.edit import FormView
from companys.forms import CompanysSearchForm
from django.db.models import Q
from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from mysite.views import LoginRequiredMixin

'''
앨범 / 포토 view 부분
'''
from companys.models import Album, Photo

def success(request):
    success1 = Pay.objects.all()  # .order_by(student__nickname)
    return render(request, 'companys/success.html', {'success1':success1})

# def success(request):
#     return render(request, 'companys/success.html')
# Create your views here.

#--- TemplateView
# class TagTV(TemplateView) :
#     template_name = 'tagging/tagging_cloud.html'

#--- ListView
class CompanysLV(ListView) :
    model = Companys
    template_name = 'companys/companys_all.html'
    context_object_name = 'companylist'
    paginate_by = 15

class TestCompanysLV(ListView) :
    #model = Post
    #queryset = Post.objects.all()[:5]
    #template_name = 'blog/post_all.html'
    template_name = 'companys/companys_test.html'
    context_object_name = 'companylist'
    paginate_by = 15

    def get_queryset(self):
        return Companys.objects.filter(Q(content__icontains = self.kwargs['word'])).distinct()

    def get_context_data(self, **kwargs):
        context = super(TestCompanysLV, self).get_context_data(**kwargs)
        context['SearchWord'] = self.kwargs['word']
        return context

# class PostTOL(TaggedObjectList) :
#     model = Post
#     template_name = 'tagging/tagging_post_list.html'

#--- DetailView
class CompanysDV(DetailView) :
    model = Companys

    # comp = Companys.objects.filter(company_name = company_name)


#--- ArchiveView
# class PostAV(ArchiveIndexView) :
#     model = Companys
#     date_field = 'modify_date'
#
# class CompanysYAV(YearArchiveView) :
#     model = Companys
#     date_field = 'modify_date'
#     make_object_list = True
#
# class CompanysMAV(MonthArchiveView) :
#     model = Companys
#     date_field = 'modify_date'
#
# class CompanysDAV(DayArchiveView) :
#     model = Companys
#     date_field = 'modify_date'
#
# class CompanysTAV(TodayArchiveView) :
#     model = Companys
    # date_field = 'modify_date'

#--- FormView
class SearchFormView(FormView):
    form_class = CompanysSearchForm
    template_name = 'companys/companys_search.html'

    def form_valid(self, form) :
        schWord = '%s' % self.request.POST['search_word']
        company_list = Companys.objects.filter(Q(company_name__icontains=schWord) | Q(location__icontains=schWord) | Q(occ__icontains=schWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = schWord
        context['object_list'] = company_list

        return render(self.request, self.template_name, context)

class CompanysCreateView(LoginRequiredMixin, CreateView):
    model = Companys
    fields = ['company_name', 'occ', 'location', 'scale', 'payment']
    initial = {'slug': 'auto-filling-do-not-input'}
    success_url = reverse_lazy('companys:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CompanysCreateView, self).form_valid(form)

class CompanysChangeLV(LoginRequiredMixin, ListView):
    template_name = 'companys/companys_change_list.html'

    def get_queryset(self):
        return Companys.objects.filter(owner=self.request.user)

class CompanysUpdateView(LoginRequiredMixin, UpdateView) :
    model = Companys
    fields = ['company_name', 'occ', 'location', 'scale', 'payment']
    success_url = reverse_lazy('companys:index')

class CompanysDeleteView(LoginRequiredMixin, DeleteView) :
    model = Companys
    success_url = reverse_lazy('companys:index')

'''
앨범 / 포토 view 부분
'''
from photo.models import Album, Photo

class AlbumLV(ListView):
    model = Album

class AlbumDV(DetailView):
    model = Album

class PhotoDV(DetailView):
    model = Photo

#--- Add/Change/Update/Delete for Photo
class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['album', 'title', 'image']
    success_url = reverse_lazy('photo:photo_detail')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PhotoCreateView, self).form_valid(form)

class PhotoChangeLV(LoginRequiredMixin, ListView):
    template_name = 'photo/photo_change_list.html'

    def get_queryset(self):
        return Photo.objects.filter(owner=self.request.user)

class PhotoUpdateView(LoginRequiredMixin, UpdateView) :
    model = Photo
    fields = ['album', 'title', 'image']
    success_url = reverse_lazy('photo:photo_detail')

class PhotoDeleteView(LoginRequiredMixin, DeleteView) :
    model = Photo
    success_url = reverse_lazy('photo:photo_detail')

#--- Add/Change/Update/Delete for Album
#--- Change/Delete for Album
class AlbumChangeLV(LoginRequiredMixin, ListView):
    template_name = 'photo/album_change_list.html'

    def get_queryset(self):
        return Album.objects.filter(owner=self.request.user)

class AlbumDeleteView(LoginRequiredMixin, DeleteView) :
    model = Album
    success_url = reverse_lazy('photo:photo_detail')


#--- InlineFormSet View
#--- Add/Update for Album
from django.shortcuts import redirect
from companys.forms import PhotoInlineFormSet

class AlbumPhotoCV(LoginRequiredMixin, CreateView):
    model = Album
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super(AlbumPhotoCV, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = PhotoInlineFormSet()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        formset = context['formset']
        for photoform in formset:
            photoform.instance.owner = self.request.user
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect('photo:album_detail', pk=self.object.id)
        else:
            return self.render_to_response(self.get_context_data(form=form))

class AlbumPhotoUV(LoginRequiredMixin, UpdateView):
    model = Album
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super(AlbumPhotoUV, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['formset'] = PhotoInlineFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.object.get_absolute_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))
