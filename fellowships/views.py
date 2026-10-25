from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from fellowships.forms import FellowshipBaseForm
from fellowships.models import Fellowship


# Create your views here.
class FellowshipListView(ListView):
    model = Fellowship
    template_name = 'fellowships/fellowship_list.html'
    context_object_name = 'fellowships'

    def get_queryset(self):
        qs = super().get_queryset()
        realm = self.request.GET.get('realm')
        if realm:
            qs = qs.filter(origin_realm__icontains=realm)
        return qs


class FellowshipDetailView(DetailView):
    model = Fellowship
    template_name = 'fellowships/fellowship_detail.html'
    context_object_name = 'fellowship'


class FellowshipCreateView(CreateView):
    model = Fellowship
    form_class = FellowshipBaseForm
    template_name = 'fellowships/fellowship_create.html'
    context_object_name = 'fellowship'
    success_url = reverse_lazy('fellowships:list')


class FellowshipUpdateView(UpdateView):
    model = Fellowship
    form_class = FellowshipBaseForm
    template_name = 'fellowships/fellowship_edit.html'
    context_object_name = 'fellowship'

    def get_success_url(self):
        return reverse('fellowships:detail', kwargs={'pk': self.object.pk})


class FellowshipDeleteView(DeleteView):
    model = Fellowship
    template_name = 'fellowships/fellowship_confirm_delete.html'
    context_object_name = 'fellowship'
    success_url = reverse_lazy('fellowships:list')
