# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the app directory contents into the container at /app
COPY app /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 for the application
EXPOSE 8080

# Define environment variables
ENV TG_BOT_TOKEN=your_telegram_bot_token
ENV TG_GROUP_CHAT_ID=your_telegram_group_chat_id

# Run app.py when the container launches
CMD ["python", "app.py"]
