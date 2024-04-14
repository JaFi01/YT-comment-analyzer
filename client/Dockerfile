
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

ENV PORT=8080
ENV HOST=0.0.0.0
ENV VITE_SERVER_URL="hidden for github"
ENV VITE_SERVER_URL_ANALYSIS="hidden for github"

EXPOSE 8080

CMD [ "npm", "run", "preview" ]