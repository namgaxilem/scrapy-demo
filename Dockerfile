FROM python:3.11.9-alpine3.19

# Create app directory
# WORKDIR /app

# Install app dependencies
# COPY src/requirements.txt ./

RUN apk update && \
    apk add git

# RUN pip install -r requirements.txt
RUN pip install scrapy scrapy-playwright 
RUN playwright install
RUN pip install wheel
RUN pip install git+https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage
RUN pip install scrapy_azure_exporter
# COPY site_search_poc ./

# Bundle app source
# COPY src /app

# EXPOSE 8080
# CMD [ "python", "server.py" ]
