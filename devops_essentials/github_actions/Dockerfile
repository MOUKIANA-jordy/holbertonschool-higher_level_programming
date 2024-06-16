# Utiliser l'image de base Alpine
FROM alpine:latest

# Installer le package curl
RUN apk add --no-cache curl

# Ajouter le fichier de configuration dans le conteneur
COPY config.txt /app/config.txt

# Set the command to echo "Hello, World!" when the container runs
CMD ["echo", "Hello, World!"]

#Create a volume whenever a container is built from this Dockerfile
VOLUME /data
