FROM google/cloud-sdk
ENV GOOGLE_APPLICATION_CREDENTIALS=key.json
ADD . /
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN pip install -r requirements.txt
#RUN gcloud auth activate-service-account --key-file=key.json

ENTRYPOINT python writer.py