from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import csv

from .models import JobApplication
from .forms import JobApplicationForm


# 🔐 User Signup
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.strip()  # ✨ prevent accidental spaces
            user.save()
            messages.success(request, 'Account created successfully! 🎉')
            return redirect('login')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


# 📊 Dashboard view per user
@login_required
def dashboard(request):
    jobs = JobApplication.objects.filter(user=request.user)

    stats = {
        'total': jobs.count(),
        'applied': jobs.filter(status='applied').count(),
        'interviews': jobs.filter(status='interview').count(),
        'offers': jobs.filter(status='offer').count(),
        'rejections': jobs.filter(status='rejected').count(),
    }

    return render(request, 'dashboard.html', {
        'jobs': jobs,
        **stats,
    })


# ➕ Add Job
@login_required
def add_job(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            messages.success(request, "✅ Job application added successfully!")
            return redirect('dashboard')
        else:
            messages.error(request, "❌ Please correct the errors below.")
    else:
        form = JobApplicationForm()

    return render(request, 'add_job.html', {
        'form': form,
        'edit': False
    })


# ✏️ Edit Job
@login_required
def edit_job(request, job_id):
    job = get_object_or_404(JobApplication, id=job_id, user=request.user)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, "✏️ Job application updated!")
            return redirect('dashboard')
        else:
            messages.error(request, "❌ Please correct the form below.")
    else:
        form = JobApplicationForm(instance=job)

    return render(request, 'add_job.html', {
        'form': form,
        'edit': True
    })


# ❌ Delete Job
@login_required
def delete_job(request, job_id):
    job = get_object_or_404(JobApplication, id=job_id, user=request.user)
    
    if request.method == 'POST':
        job.delete()
        messages.success(request, "🗑️ Job deleted.")
        return redirect('dashboard')
    
    return render(request, 'confirm_delete.html', {'job': job})


# 📤 Export Jobs to CSV
@login_required
def export_jobs_csv(request):
    jobs = JobApplication.objects.filter(user=request.user)

    response = HttpResponse(content_type='text/csv')
    filename = f"{request.user.username}_jobs.csv"
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    writer = csv.writer(response)
    writer.writerow(['Job Title', 'Company Name', 'Location', 'Status', 'Date Applied'])

    for job in jobs:
        writer.writerow([
            job.job_title,
            job.company_name,
            job.location,
            job.status,
            job.date_applied
        ])

    return response


# 🧾 Export Jobs to PDF
@login_required
def export_jobs_pdf(request):
    jobs = JobApplication.objects.filter(user=request.user)

    template_path = 'pdf_template.html'
    context = {
        'jobs': jobs,
        'user': request.user
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="job_applications_{request.user.username}.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('❌ PDF rendering error occurred.')

    return response