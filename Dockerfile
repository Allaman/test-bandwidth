FROM python:slim

ENV INSTALL_DIR /var/opt/app/

RUN mkdir $INSTALL_DIR mkdir

COPY . $INSTALL_DIR

RUN apt-get -y update &&\
    apt-get -y upgrade &&\
    pip install --upgrade pip

WORKDIR $INSTALL_DIR

RUN pip install --user --no-cache-dir --no-warn-script-location -r requirements.txt

WORKDIR $INSTALL_DIR/vis-bandwidth

ENTRYPOINT [ "python", "./main.py", "--cmd" ]
CMD [ ]