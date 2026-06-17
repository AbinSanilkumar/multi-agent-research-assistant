from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from agents.planner import generate_research_plan
from agents.researcher import generate_research_content

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

            try:

                plan = generate_research_plan(topic)

            except Exception as e:

                print(f"Planner Error: {e}")

                plan = "Unable to generate plan at this time."

            ResearchSession.objects.create(
                user=request.user,
                topic=topic,
                plan=plan
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


@login_required
def generate_research(request, session_id):

    session = get_object_or_404(
        ResearchSession,
        id=session_id,
        user=request.user
    )

    if not session.research_content:

        try:

            content = generate_research_content(
                session.topic,
                session.plan
            )

            session.research_content = content

            session.save()

        except Exception as e:

            print(f"Gemini Error: {e}")

    return redirect('home')


@login_required
def session_detail(request, session_id):

    session = get_object_or_404(
        ResearchSession,
        id=session_id,
        user=request.user
    )

    context = {
        'session': session
    }

    return render(
        request,
        'research/session_detail.html',
        context
    )