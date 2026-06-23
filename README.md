# Multi-Agent Research Assistant

An AI-powered research platform that uses multiple specialized AI agents to automate the complete research workflow, from planning and content generation to fact verification, report writing, and PDF export.

---

## Overview

Multi-Agent Research Assistant is a Django-based AI application that orchestrates multiple AI agents to perform research tasks automatically.

The system allows users to:

* Create research sessions
* Generate structured research plans
* Produce detailed research content
* Verify research findings
* Generate professional reports
* Export reports as PDF documents

The project demonstrates AI workflow orchestration, agent-based architecture, authentication, database integration, and document generation.

---

## Features

### Authentication

* User Registration
* User Login
* User Logout
* Session-based Authentication

### Research Management

* Create Research Sessions
* Track Research Progress
* View Previous Sessions
* Delete Sessions

### AI Agents

#### Planner Agent

Creates a structured research outline for the selected topic.

#### Research Agent

Generates detailed research content based on the generated plan.

#### Fact Checker Agent

Reviews generated research and provides:

* Confidence Score
* Verified Claims
* Potential Issues

#### Report Writer Agent

Produces a professional final report using:

* Research Content
* Fact Check Results
* Verified Insights

### PDF Export

* Download final reports as PDF documents.

### Dashboard Analytics

* Total Sessions
* Completed Sessions
* Pending Sessions

### Workflow Tracking

Visual progress tracking for:

* Planner
* Research
* Fact Check
* Report Generation

---

## System Architecture

User
│
▼
Research Session
│
▼
Planner Agent
│
▼
Research Agent
│
▼
Fact Checker Agent
│
▼
Report Writer Agent
│
▼
PDF Export

---

## Technology Stack

### Backend

* Django 6
* Python 3

### AI

* Google Gemini API

### Database

* SQLite

### Frontend

* HTML
* CSS
* Bootstrap 5

### PDF Generation

* ReportLab

---

## Project Workflow

1. User creates a research topic.
2. Planner Agent generates a research plan.
3. Research Agent creates detailed research content.
4. Fact Checker Agent evaluates the content and assigns a confidence score.
5. Report Writer Agent generates a professional report.
6. User exports the report as a PDF.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/AbinSanilkumar/multi-agent-research-assistant.git
cd multi-agent-research-assistant
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create .env file:

```env
GEMINI_API_KEY=your_api_key
```

Apply migrations:

```bash
python manage.py migrate
```

Run server:

```bash
python manage.py runserver
```

---

## Current Status

### Completed

* Project Setup
* User Authentication
* Research Dashboard
* Planner Agent
* Research Agent
* Fact Checker Agent
* Report Writer Agent
* Session Detail Page
* PDF Export
* Workflow Progress Tracking
* Dashboard Analytics
* UI Improvements

### Upcoming

* Deployment
* Gemini SDK Migration (`google.genai`)
* RAG Integration
* Document Upload Support
* Vector Database Integration
* Citation Generation

---

## Future Enhancements

### RAG Pipeline

Upload Documents
│
▼
Chunking
│
▼
Embeddings
│
▼
Vector Database
│
▼
Context-Aware Research

### Additional Features

* Multi-Document Research
* Research History Analytics
* Team Collaboration
* Export to DOCX
* Research Templates

---

## Author

Abin 

Final Year AIML Student

Built as an AI Engineering and Full-Stack Development Project.
