from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from characters.forms import CharacterBaseForm, CharacterEditForm
from characters.models import Character


# Create your views here.
class CharacterListView(ListView):
    model = Character
    template_name = 'characters/character_list.html'
    context_object_name = 'characters'

    def get_queryset(self):
        qs = super().get_queryset()
        race = self.request.GET.get('race')
        if race:
            qs = qs.filter(race__icontains=race)
        sort = self.request.GET.get('sort')
        if sort == 'power':
            qs = qs.order_by('-combat_power')
        elif sort == 'fellowship':
            qs = qs.order_by('-fellowship__name')
        elif sort == 'name':
            qs = qs.order_by('name')
        return qs

class CharacterDetailView(DetailView):
    model = Character
    template_name = 'characters/character_detail.html'
    context_object_name = 'character'

class CharacterCreateView(CreateView):
    model = Character
    template_name = 'characters/character_create.html'
    context_object_name = 'character'

    form_class = CharacterBaseForm
    success_url = reverse_lazy('characters:list')

class CharacterUpdateView(UpdateView):
    model = Character
    template_name = 'characters/character_edit.html'
    context_object_name = 'character'

    form_class = CharacterEditForm

    def get_success_url(self):
        return reverse('characters:detail', kwargs={'pk': self.object.pk})

class CharacterDeleteView(DeleteView):
    model = Character
    template_name = 'characters/character_confirm_delete.html'
    context_object_name = 'character'
    success_url = reverse_lazy('characters:list')