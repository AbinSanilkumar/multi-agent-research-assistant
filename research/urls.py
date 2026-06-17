from django.urls import path
from .views import home, generate_research, session_detail

urlpatterns = [
    path('', home, name='home'),

    path(
        'generate-research/<int:session_id>/',
        generate_research,
        name='generate_research'
    ),

    path(
        'session/<int:session_id>/',
        session_detail,
        name='session_detail'
    ),
]