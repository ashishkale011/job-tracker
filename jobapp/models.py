from django.db import models
from django.contrib.auth.models import User

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('interview', 'Interview'),
        ('offer', 'Offer'),
        ('rejected', 'Rejected'),
    ]

    # 👤 Link job to logged-in user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # 📄 Job details
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date_applied = models.DateField()

    # 📊 Application status
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    # ✅ Checkbox
    resume_sent = models.BooleanField(default=False)

    # 🗒️ Notes or comments
    notes = models.TextField(blank=True)

    # 📎 Resume file upload (optional)
    resume_file = models.FileField(upload_to='resumes/', blank=True, null=True)

    def __str__(self):
        # 🧾 Show job title nicely in admin and logs
        return f"{self.job_title} at {self.company_name} [{self.user.username}]"