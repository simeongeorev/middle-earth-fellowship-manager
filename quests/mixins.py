from fellowships.models import Fellowship


class QuestFellowshipStatusMixin:
    def form_valid(self, form):
        response = super().form_valid(form)
        for fellowship in Fellowship.objects.all():
            fellowship.update_status()
        return response
