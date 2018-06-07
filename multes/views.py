from django.shortcuts import render
from django.forms import modelform_factory
from multes.models import Multa
from django import forms
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q
from multes.models import Persona
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from .forms import CraftForm, CommentForm
from .models import CraftPost, Comment
from django.utils import timezone

def posa_multa(request, id=None):
    if bool(id):
        unaMulta = get_object_or_404(Multa, pk=id)
    else:
        unaMulta =  Multa()
    form_class1 = modelform_factory(Multa, exclude=[], widgets={}) #'persona': forms.HiddenInput()} )

    if request.method == 'POST':
        form1 = form_class1(request.POST, instance = unaMulta)
        if form1.is_valid():
            form1.save()
            return redirect('posa_multa')
    else:
        form1 = form_class1(instance = unaMulta)
    for f in form1.fields:
        form1.fields[f].widget.attrs['class'] = 'form-control'

    widget_persona = form1.fields['persona'].widget

    if bool(id) and hasattr(unaMulta, 'persona'):
        widget_persona.choices = [(unaMulta.persona.pk,
                                    unaMulta.persona.cognom + ', ' + unaMulta.persona.nom
                                    ), ]
    else:
        widget_persona.choices = [(u'', u'---------'),]

    craftposts = CraftPost.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(craftposts, 6)
    try:
        craftposts = paginator.page(page)
    except PageNotAnInteger:
        craftposts = paginator.page(1)
    except EmptyPage:
        craftposts = paginator.page(paginator.num_pages)

    craftposts1 = CraftPost.objects.active()
    query = request.GET.get("q")
    if query:
        craftposts = craftposts1.filter(Q(title__icontains=query) | Q(text__icontains=query)).distinct()
    paginator = Paginator(craftposts1, 2)

    return render(request,
                 'multes/posa_multa.html',
                  {'form1': form1,'craftposts': craftposts}
              )


def craft_detail(request, pk):
   craftpost = get_object_or_404(CraftPost, pk=pk)
   if request.method == "POST":
      form = CommentForm(request.POST)
      if form.is_valid():
         comment = form.save(commit=False)
         if comment.author:
            comment.name = comment.author
         else:
            comment.name = request.user
         comment.craftpost = craftpost
         comment.save()
         return redirect('multes:craft_detail', pk=craftpost.pk)
   else:
      form = CommentForm()
   return render(request, 'multes/craft_detail.html', {'form': form, 'craftpost': craftpost})
#
@login_required
def craft_new(request):
   if request.method == "POST":
      form = CraftForm(request.POST, request.FILES)
      if form.is_valid():
         craftpost = form.save(commit=False)
         craftpost.author = request.user
         craftpost.save()
         return redirect('multes:posa_multa')

   else:
      form = CraftForm()
   return render(request, 'multes/craft_edit.html', {'form': form})

@login_required
def craft_edit(request, pk):
   craftpost = get_object_or_404(CraftPost, pk=pk)
   if request.method == "POST":
      form = CraftForm(request.POST, request.FILES, instance=craftpost, )
      if form.is_valid():
         craftpost = form.save(commit=False)
         craftpost.author = request.user
         craftpost.save()
         return redirect('multes:posa_multa')
   else:
      form = CraftForm(instance=craftpost)
   return render(request, 'multes/craft_edit.html', {'form': form})
#
@login_required
def craft_draft_list(request):
   draftposts = CraftPost.objects.filter(
       published_date__lte=timezone.now()).order_by('-published_date')
   page = request.GET.get('page', 1)
   paginator = Paginator(draftposts, 6)
   try:
      draftposts = paginator.page(page)
   except PageNotAnInteger:
      draftposts = paginator.page(1)
   except EmptyPage:
      draftposts = paginator.page(paginator.num_pages)
   return render(request, 'multes/craft_draft_list.html', {'draftposts': draftposts})
#
def craft_publish(request, pk):
   craftpost = get_object_or_404(CraftPost, pk=pk)
   craftpost.publish()
   return redirect('multes:craft_detail', pk=pk)
#
@login_required
def craft_remove(request, pk):
   craftpost = get_object_or_404(CraftPost, pk=pk)
   craftpost.delete()
   return redirect('multes:posa_multa')
#
@login_required
def comment_approve(request, pk):
   comment = get_object_or_404(Comment, pk=pk)
   comment.approve()
   return redirect('multes:craft_detail', pk=comment.craftpost.pk)
#
@login_required
def comment_remove(request, pk):
   comment = get_object_or_404(Comment, pk=pk)
   craft_pk = comment.craftpost.pk
   comment.delete()
   return redirect('multes:craft_detail', pk=comment.craftpost.pk)
#
def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

def persones_api(request):
    q = request.GET.get('q','')
    p = request.GET.get('page',1)
    q_nom = Q( nom__icontains = q )
    q_cognom = Q( cognom__icontains = q )
    totes_les_persones = Persona.objects.filter( q_nom | q_cognom ).order_by('cognom','nom')
    persones_paginades = Paginator(totes_les_persones, 10)
    pagina = persones_paginades.page( p )

    resultat = {
               'persones': [ { 'id': p.pk, 'text': p.cognom + ', ' + p.nom }
                             for p in pagina  ],
                    'more': pagina.has_next()
   }

    resultat_serialitzat = json.dumps(resultat )
    return HttpResponse( resultat_serialitzat, content_type="application/json" )
