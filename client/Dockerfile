FROM oven/bun:1-alpine

WORKDIR /app

COPY package.json bun.lock* ./

RUN bun install --frozen-lockfile

COPY . .

ARG VITE_SERVER_URL=http://localhost:5000
ARG VITE_SERVER_URL_ANALYSIS=http://localhost:5000/analyze_video
ENV VITE_SERVER_URL=$VITE_SERVER_URL
ENV VITE_SERVER_URL_ANALYSIS=$VITE_SERVER_URL_ANALYSIS

RUN bun run build

ENV PORT=8080
ENV HOST=0.0.0.0

EXPOSE 8080

CMD [ "bun", "run", "preview" ]
