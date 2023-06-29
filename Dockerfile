ARG PYTHON_VERSION=3.9-slim-buster

FROM python:${PYTHON_VERSION} as python

# FROM python:3.11.4

ENV PYTHONUNBUFFERED=1

WORKDIR /employeeManger

COPY requirements.txt .

# If building behind an http_proxy, set them for git and npm
# RUN git config --global http.proxy http://proxy.hcm.fpt.vn:80 && \
#     npm config set proxy http://proxy.hcm.fpt.vn:80 && \
#     npm config set https-proxy http://proxy.hcm.fpt.vn:80

# Install dependencies
# RUN npm install

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py","runserver"]