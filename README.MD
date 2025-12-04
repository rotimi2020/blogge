```markdown
# ProjectBlog - Django Blog Application

A Django-based blog application with user authentication and content management.

## Features
- User authentication
- Blog post creation and management
- Media uploads
- Admin dashboard

## Installation

1. Clone the repository:
```bash
git clone https://github.com/rotimi2020/blogge.git
cd blogge
```

2. Create a virtual environment:
```bash
# On Mac/Linux
python -m venv venv
source venv/bin/activate

# On Windows (Git Bash / CMD / PowerShell)
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with your settings:
```
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

5. Run database migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to see the app.

## Deployment

This project is configured for deployment on Render.com.

1. Connect your GitHub repository to Render.
2. Set environment variables (`SECRET_KEY`, `DEBUG`, etc.).
3. Build command:
```bash
bash build.sh
```
4. Start command is handled by Procfile:
```
web: gunicorn blogge.wsgi
```

## License

MIT License
```
