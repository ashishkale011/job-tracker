# Job Application Tracker

A modern Django web app to **track, manage, and analyze your job applications**.  
Add jobs, upload resumes, monitor interview progress, and export your data — all in one place!

---

## 🚀 Features

- User Registration & Login
- Add/Edit/Delete Job Applications
- Upload Resume for Each Job
- Dashboard with Stats (Total, Interviews, Offers, Rejections)
- Export to PDF & CSV
- Admin Panel (Django Admin)
- Password Reset
- Mobile Responsive UI (Bootstrap)
- Role-based Access (User/Admin)
- Clean, Modern Design

---

## 🛠️ Tech Stack

- **Backend:** Django 5.x
- **Frontend:** Bootstrap 5, HTML, CSS
- **Database:** SQLite (easy to switch to PostgreSQL)
- **PDF Export:** xhtml2pdf
- **Form Styling:** django-widget-tweaks

---

## 🏁 Getting Started (Local Setup)

1. **Clone the repo:**
   ```bash
   git clone https://github.com/yourusername/job-tracker.git
   cd job-tracker

2. Create & activate virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1   # (Windows PowerShell)
   # or CMD: venv\Scripts\activate

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. Create superuser (for admin panel):
   ```bash
   python manage.py createsuperuser

6. Run the server:
   ```bash
   python manage.py runserver

7. Open in browser:
   http://127.0.0.1:8000/
