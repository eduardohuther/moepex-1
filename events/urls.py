from django.urls import path
from django.contrib.auth.decorators import login_required

from events import views as views_events


urlpatterns = [
    path('experimento/<int:pk>/', views_events.ExperimentDetailView.as_view(), name='experiment-detail'),
    path('minicurso/<int:pk>/', views_events.EventDetailView.as_view(), name='event-detail'),

    path('meus-eventos/', login_required(views_events.MyRegistrationsListView.as_view()), name='my-events'),
    path('experimento/novo/', login_required(views_events.ExperimentCreateView.as_view()), name='experiment-create'),
    path('minicurso/novo/', login_required(views_events.EventCreateView.as_view()), name='event-create'),
    path('minicurso/<int:pk>/turmas/', login_required(views_events.GroupListView.as_view()), name='group-list'),
    path('minicurso/inscricao/<int:pk>/', login_required(views_events.EventRegistrationView.as_view()), name="event-registration"),
    path('minicurso/<int:pk>/turmas/nova/', login_required(views_events.GroupCreateView.as_view()), name='group-create'),
]
