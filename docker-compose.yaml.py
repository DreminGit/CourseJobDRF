services:

  redis:
    image: redis:latest
    restart: on-failure


  db:
    image: postgres:17
    restart: on-failure
    env_file:
      - .env
    expose:
      - "5432"
    volumes:
      - pg_data:/var/lib/postgresql/data
    healthcheck:
      test: [ "CMD-SHELL", "-c", "pg_isready -U $POSTGRES_USER" ]
      interval: 10s
      retries: 5
      timeout: 5s


  app:
    build: .
    tty: true
    ports:
      - "8000:8000"
    command: sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8001"
    depends_on:
      db:
        condition: service_healthy
    volumes:
      - .:/app

  celery:
    build: .
    tty: true
    command: celery -A config worker -l INFO
    restart: on-failure
    volumes:
      - .:/app
    depends_on:
      - redis
      - db
      - app

  celery-beat:
    build: .
    tty: true
    command: celery -A config worker -l INFO
    restart: on-failure
    volumes:
      - .:/app
    depends_on:
      - redis
      - db
      - app

volumes:
  pg_data: