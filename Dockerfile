FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set environment variables
ENV CHAINLIT_HOST=0.0.0.0
ENV CHAINLIT_PORT=8000

EXPOSE 8000

CMD ["chainlit", "run", "app.py"] 