FROM ubuntu

RUN apt update && apt -y upgrade
RUN apt install -y git python3 python3-pip
RUN apt install -y curl
RUN pip3 install essential_generators

RUN pip install fastapi
RUN pip install uvicorn

RUN git init
RUN git clone https://github.com/MickChristie/opensource3

EXPOSE 8080
CMD ["uvicorn", "main:app1", "--reload", "port=8080"]

