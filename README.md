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


✅ How to Run Your Django Project (Step-by-Step)

1️⃣ Open VS Code

Open your project folder (the one with manage.py).


2️⃣ Activate Virtual Environment
In PowerShell (VS Code terminal):
PowerShell

=> .\venv\Scripts\Activate.ps1       


3️⃣ Install Dependencies
Bash

=> pip install -r requirements.txt          


4️⃣ Apply Migrations
Bash
=> python manage.py makemigrations     

=> python manage.py migrate      


5️⃣ Create Superuser (for admin panel)
Bash

=> python manage.py createsuperuser     


6️⃣ Run the Development Server
Bash

=> python manage.py runserver     


7️⃣ Open Browser and Visit:

=> Main site:
http://127.0.0.1:8000/

=>	Admin panel:
http://127.0.0.1:8000/admin/

