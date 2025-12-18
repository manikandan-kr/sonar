FROM python:3.11-slim

WORKDIR /app

COPY . .
# RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -e .[dev]

EXPOSE 8080

CMD [
  "uvicorn",
  "analytics_mcp.server:app",
  "--host", "0.0.0.0",
  "--port", "8080",
  "--proxy-headers",
  "--forwarded-allow-ips", "*"
]
