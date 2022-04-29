FROM python:3.10

COPY ./requirements.txt /root/requirements.txt

RUN pip install --upgrade pip && \
    pip install --ignore-installed -r /root/requirements.txt

WORKDIR /root/dcim_test

COPY . /root/dcim_test


CMD [ "python", "main.py" ]