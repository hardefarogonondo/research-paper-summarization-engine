FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /streamlit_app

COPY ./src/frontend /streamlit_app

RUN pip install --no-cache-dir -r requirements_frontend.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]