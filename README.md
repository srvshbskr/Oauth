# Username Availability Checker

This project is a Django-based site that checks the availability of usernames and implements Single Sign-On (SSO) using the `social-auth-app-django` package.

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/srvshbskr/Oauth.git
   cd Oauth
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   
3. **Migrate changes:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

4. **Create Super user:**
   ```bash
   python manage.py createsuperuser

5. **Run server:**

   Finally, start the app by using

   ```bash
   python manage.py runserver
