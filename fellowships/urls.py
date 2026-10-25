from django.urls import path, include

from fellowships.views import FellowshipListView, FellowshipDetailView, FellowshipCreateView, FellowshipUpdateView, \
    FellowshipDeleteView

app_name = 'fellowships'

urlpatterns = [
    path('', FellowshipListView.as_view(), name='list'),
    path('create/', FellowshipCreateView.as_view(), name='create'),
    path('<int:pk>/', include([
        path('detail/', FellowshipDetailView.as_view(), name='detail'),
        path('edit/', FellowshipUpdateView.as_view(), name='edit'),
        path('delete/', FellowshipDeleteView.as_view(), name='delete'),
    ]))
]
