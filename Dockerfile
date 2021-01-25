FROM python:3.6

# install os dependencies (NodeJS)
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get update && apt-get install -y nodejs

# change TZ to Melbourne (replace with your time zone or remove for UTC)
RUN rm -f /etc/localtime && ln -s /usr/share/zoneinfo/Australia/Melbourne /etc/localtime

# declare app directory
WORKDIR /app

COPY requirements.txt .
# install (internal) pip dependencies
RUN pip install -r requirements.txt
# mongo / abc fix (https://github.com/py-bson/bson/issues/82#issuecomment-428398316)
RUN pip uninstall -y bson pymongo
RUN pip install pymongo

# install NPM dependencies
COPY package.json .
# install npm dependencies
RUN npm i

# copy javascript code
COPY frontend ./frontend
# TODO: re-enable this if you provide any static resources
# COPY static ./static

COPY .babelrc .
COPY webpack.config.js .

# build frontend
RUN npm run build

# copy python code
COPY api ./api
COPY storage ./storage
COPY config.py .
COPY runner.py .

# start server
ENTRYPOINT ["python3"]
CMD ["runner.py"]
