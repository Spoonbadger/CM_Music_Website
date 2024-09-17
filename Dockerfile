FROM python:3
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]


# You can place this Dockerfile in the root of your Django project and build it with:

#    docker build -t your-app-name .
#    Then, run the container with:
    
#    docker run -p 8000:8000 your-app-name

#    This will start the Django development server, accessible at http://localhost:8000.