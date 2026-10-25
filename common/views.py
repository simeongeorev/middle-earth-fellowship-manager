from django.views.generic import TemplateView

from characters.models import Character
from fellowships.models import Fellowship
from quests.models import Quest


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_fellowships'] = Fellowship.objects.count()
        context['total_characters'] = Character.objects.count()
        context['total_quests'] = Quest.objects.count()
        return context