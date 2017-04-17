FROM python:2.7-alpine

ADD https://github.com/alexellis/faas/releases/download/v0.3-alpha/fwatchdog /usr/bin
RUN chmod +x /usr/bin/fwatchdog

WORKDIR /app
COPY main.py /app

ENV fprocess='python main.py'
CMD ["fwatchdog"]
