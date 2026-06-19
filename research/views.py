from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from agents.planner import generate_research_plan
from agents.researcher import generate_research_content
from agents.fact_checker import fact_check_content
from agents.report_writer import generate_final_report

from .forms import ResearchForm
from .models import ResearchSession

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import io


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

    total_sessions = ResearchSession.objects.filter(
        user=request.user
    ).count()

    completed_sessions = ResearchSession.objects.filter(
        user=request.user,
        status='completed'
    ).count()

    pending_sessions = ResearchSession.objects.filter(
        user=request.user,
        status='pending'
    ).count()

    context = {
        'form': form,
        'sessions': sessions,
        'total_sessions': total_sessions,
        'completed_sessions': completed_sessions,
        'pending_sessions': pending_sessions,
    }

    return render(request, 'research/dashboard.html', context)


@login_required
def generate_research(request, session_id):
    session = get_object_or_404(ResearchSession, id=session_id, user=request.user)
    if not session.research_content:
        try:
            content = generate_research_content(session.topic, session.plan)
            session.research_content = content
            session.status = "completed"
            session.save()
        except Exception as e:
            session.research_content = f"Research generation failed.\n\nError:\n{str(e)}"
            session.save()
    return redirect('home')


@login_required
def session_detail(request, session_id):
    session = get_object_or_404(ResearchSession, id=session_id, user=request.user)
    context = {'session': session}
    return render(request, 'research/session_detail.html', context)


@login_required
def generate_fact_check(request, session_id):
    session = get_object_or_404(ResearchSession, id=session_id, user=request.user)
    if session.research_content and not session.fact_check_report:
        try:
            result = fact_check_content(session.research_content)
            session.fact_check_report = result["report"]
            session.confidence_score = result["score"]
            session.save()
        except Exception as e:
            print(f"Fact Check Error: {e}")
    return redirect('session_detail', session_id=session.id)


@login_required
def generate_report(request, session_id):
    session = get_object_or_404(ResearchSession, id=session_id, user=request.user)
    if session.research_content and session.fact_check_report and not session.final_report:
        try:
            report = generate_final_report(session.topic, session.research_content, session.fact_check_report)
            session.final_report = report
            session.save()
        except Exception as e:
            print(f"Report Error: {e}")
    return redirect('session_detail', session_id=session.id)


@login_required
def delete_session(request, session_id):
    session = get_object_or_404(ResearchSession, id=session_id, user=request.user)
    session.delete()
    return redirect('home')


@login_required
def download_report(request, session_id):
    session = get_object_or_404(ResearchSession, id=session_id, user=request.user)

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph(f"Research Report: {session.topic}", styles['Title']))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph(f"Confidence Score: {session.confidence_score}%", styles['Heading2']))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph(session.final_report.replace("\n", "<br/>"), styles['BodyText']))

    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{session.topic}.pdf"'
    return response
