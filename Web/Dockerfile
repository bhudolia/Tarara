# The Node version that we'll be running for our version of React.
# You may have to search the Node directory for a version that fits
# the version of React you're using.
FROM node:8.9-alpine

# Create a work directory and copy over our dependency manifest files.
RUN mkdir /app
WORKDIR /app

COPY ./src ./src
COPY ./public ./public
COPY ["package.json", "package-lock.json*", "./"]

# add `/app/node_modules/.bin` to $PATH
ENV NODE_PATH=/node_modules
ENV PATH=$PATH:/node_modules/.bin

RUN npm install
# If you're using yarn:
#  yarn build
RUN npm install --production --silent && mv node_modules ../
RUN ls -al

CMD npm start
# Expose PORT 3000 on our virtual machine so we can run our server
EXPOSE 3000


