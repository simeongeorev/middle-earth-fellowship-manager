from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from quests.forms import QuestBaseForm
from quests.mixins import QuestFellowshipStatusMixin
from quests.models import Quest

# Create your views here.
class QuestListView(ListView):
    model = Quest
    template_name = 'quests/quest_list.html'
    context_object_name = 'quests'

    def get_queryset(self):
        qs = super().get_queryset()
        sort = self.request.GET.get('sort')
        if sort == 'region':
            qs = qs.order_by('region')
        elif sort == 'threat_level':
            qs = qs.order_by('threat_level')
        return qs


class QuestCreateView(QuestFellowshipStatusMixin, CreateView):
    model = Quest
    template_name = 'quests/quest_create.html'
    context_object_name = 'quest'

    form_class = QuestBaseForm
    success_url = reverse_lazy('quests:list')


class QuestUpdateView(QuestFellowshipStatusMixin, UpdateView):
    model = Quest
    template_name = 'quests/quest_edit.html'
    context_object_name = 'quest'

    form_class = QuestBaseForm
    success_url = reverse_lazy('quests:list')


class QuestDeleteView(QuestFellowshipStatusMixin, DeleteView):
    model = Quest
    template_name = 'quests/quest_confirm_delete.html'
    context_object_name = 'quest'
    success_url = reverse_lazy('quests:list')

