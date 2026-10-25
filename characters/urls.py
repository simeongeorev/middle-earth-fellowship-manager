from django.urls import path, include

from characters.views import CharacterListView, CharacterCreateView, CharacterDetailView, CharacterUpdateView, \
    CharacterDeleteView

app_name = 'characters'

urlpatterns = [
    path('', CharacterListView.as_view(), name='list'),
    path('create/', CharacterCreateView.as_view(), name='create'),
    path('<int:pk>/', include([
        path('detail/', CharacterDetailView.as_view(), name='detail'),
        path('edit/', CharacterUpdateView.as_view(), name='edit'),
        path('delete/', CharacterDeleteView.as_view(), name='delete'),
    ]))
]
