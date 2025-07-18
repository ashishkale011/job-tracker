from django.contrib import admin
from .models import JobApplication
from django.contrib.auth.models import User

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    # 🧾 Fields shown in admin list
    list_display = (
        'job_title',
        'company_name',
        'location',
        'status',
        'date_applied',
        'resume_sent',
        'user',
    )

    # 🔍 Searchable fields
    search_fields = (
        'job_title',
        'company_name',
        'location',
        'status',
        'notes',
        'user__username',
    )

    # 📂 Sidebar filters
    list_filter = (
        'status',
        'resume_sent',
        'date_applied',
        'user',
    )

    # 🔽 Order latest job first
    ordering = ('-date_applied',)

    # ✏️ Editable in list view
    list_editable = ('status', 'resume_sent')

    # ✅ Optional — Customize the user dropdown in form
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.order_by("username")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # 🛠 Automatically set user if missing (e.g. from frontend)
    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        super().save_model(request, obj, form, change)