#Base Image for postgres
FROM postgres:latest

#Environment variables
ENV POSTGRES_PASSWORD=Qwerty@12345
ENV POSTGRES_USER=postgres
ENV POSTGRES_DB=postgres

#Copy files to docker working directory
COPY create_EventsMetadata.sql /docker-entrypoint-initdb.d/create_EventsMetadata.sql

#Declare the postgres server port
EXPOSE 5432