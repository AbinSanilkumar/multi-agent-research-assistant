from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import ResearchForm
from .models import ResearchSession


@login_required
def home(request):
    return dashboard(request)


@login_required
def dashboard(request):

    form = ResearchForm()

    sessions = ResearchSession.objects.filter(
        user=request.user
    ).order_by('-created_at')

    context = {
        'form': form,
        'sessions': sessions
    }

    return render(
        request,
        'research/dashboard.html',
        context
    )