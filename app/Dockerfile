#Base Image for python
FROM python:3.8

#Environment variables
ENV PYTHONUNBUFFERED 1

#Set working directory
WORKDIR /WebScraping

#Copy files to docker working directory
COPY futureDemandCoding.py .
COPY requirements.txt .

#Install additional packages from requirements.txt
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["futureDemandCoding.py"]