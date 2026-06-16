from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from agents.orchestrator import run_research_workflow

from .forms import ResearchForm
from .models import ResearchSession


@login_required
def home(request):
    return dashboard(request)


@login_required
def dashboard(request):

    if request.method == 'POST':

        form = ResearchForm(request.POST)

        if form.is_valid():

            topic = form.cleaned_data['topic']

            result = run_research_workflow(topic)

            ResearchSession.objects.create(
                user=request.user,
                topic=topic,
                plan=result["plan"],
                research_content=result["research_content"]
            )

            return redirect('home')

    else:

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