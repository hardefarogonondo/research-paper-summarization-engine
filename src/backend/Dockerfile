FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./src/backend /app
COPY ./models/pegasus_model /app/models/pegasus_model

RUN pip install --no-cache-dir -r requirements_backend.txt
RUN pip install --no-cache-dir torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu121
RUN pip install --no-cache-dir transformers sentencepiece

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]