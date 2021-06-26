FROM openjdk:11-jdk-slim
RUN apt update
RUN apt install software-properties-common -y
RUN apt install python3.7 -y
COPY target/boca-0.0.1-SNAPSHOT.jar /app.jar
COPY temp /temp
ENTRYPOINT ["java","-jar","/app.jar"]
