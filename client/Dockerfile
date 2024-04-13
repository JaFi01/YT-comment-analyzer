# Użyj obrazu node do budowy aplikacji
FROM node:20 AS builder

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Skopiuj pliki projektu
COPY . .

# Zainstaluj zależności i zbuduj aplikację
RUN npm install
RUN npm run build

# Utwórz obraz z budowaną aplikacją
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
