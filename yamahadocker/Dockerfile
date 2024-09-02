FROM python:3.8

ENV PYTHONUNBUFFERED=1

# Create and set the working directory
RUN mkdir /code
WORKDIR /code

# Copy only requirements.txt first to leverage Docker cache
COPY requirements.txt /code/

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . /code/

# Expose the port the app runs on
EXPOSE 8000

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
