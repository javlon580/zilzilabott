FROM python:3.11-slim

WORKDIR /app

# Copy everything FIRST (simplest approach)
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Debug: List files to confirm
RUN echo "=== FILES IN CONTAINER ===" && ls -la

# Run the bot
CMD ["python", "bot.py"]