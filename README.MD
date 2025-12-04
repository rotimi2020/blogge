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
git clone https://github.com/yourusername/projectblog.git
cd projectblog
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create .env file with your settings

5. Run migrations:
```bash
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## Deployment
This project is configured for deployment on Render.com

## License
MIT License