FROM python:3.9
WORKDIR /usr/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
COPY model ./model
EXPOSE 5000
CMD ["python","app.py"]