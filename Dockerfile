FROM nikolaik/python-nodejs:latest as development
WORKDIR /usr/src/app
RUN pip install scikit-learn numpy pandas simplejson
COPY ./package.json ./index.js  ./
RUN npm install
COPY ./ ./
ENV PORT 8000
EXPOSE $PORT


# Production mode
FROM nikolaik/python-nodejs:latest as production
RUN pip install scikit-learn numpy pandas simplejson
ARG NODE_ENV=production
ENV NODE_ENV=${NODE_ENV}
WORKDIR /usr/src/app
COPY --from=development /usr/src/app ./
ENV PORT 8000
EXPOSE $PORT
CMD ["node", "index"]