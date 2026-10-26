from django.urls import path, include

from quests.views import QuestListView, QuestCreateView, QuestUpdateView, QuestDeleteView

app_name = 'quests'

urlpatterns = [
    path('', QuestListView.as_view(), name='list'),
    path('create/', QuestCreateView.as_view(), name='create'),
    path('<int:pk>/', include([
        path('edit/', QuestUpdateView.as_view(), name='edit'),
        path('delete/', QuestDeleteView.as_view(), name='delete'),
    ]))
]