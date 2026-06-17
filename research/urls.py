from django.urls import path
from .views import home, generate_research

urlpatterns = [
    path('', home, name='home'),

    path(
        'generate-research/<int:session_id>/',
        generate_research,
        name='generate_research'
    ),
]