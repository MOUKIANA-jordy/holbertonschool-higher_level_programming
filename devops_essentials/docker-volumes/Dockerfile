# Use the Alpine base image
FROM alpine:latest

#Install the curl package
RUN apk add --no-cache curl

#file to a suitable location in the container
COPY hello.txt /app/hello.txt

# Set the command to echo "Hello, World!" when the container runs
CMD ["echo", "Hello, World!"]

# Create a volume at /data
VOLUME /data
