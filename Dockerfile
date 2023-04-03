FROM ubuntu:22.04

ENV TZ=Europe/London 
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt-get install -y python3.10 pip python3-dev build-essential
RUN pip install --upgrade pip 
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
RUN playwright install 
RUN playwright install-deps
COPY config /app/config 
COPY lexicon /app/lexicon 
COPY pars /app/pars 
COPY utils /app/utils 
COPY main.py /app/main.py 
CMD [ "python3", "main.py" ]