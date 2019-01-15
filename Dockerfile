FROM python:3

WORKDIR /usr/src/app

ADD . /PDFParser

COPY requirements.txt ./
COPY sources.list /etc/apt/

RUN apt-get update
RUN apt-get install -y build-essential libpoppler-cpp-dev xpdf vim-tiny
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pdftotext
RUN export PATH=$PATH:/usr/local/lib/python2.7/site-packages

COPY . .
COPY ./dossier/* ./dossier/

CMD [ "bash" ]
