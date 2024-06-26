Docker volumes are a mechanism to persist data generated by and used by Docker containers. Unlike a bind mount, which mounts any directory from the host into the container, a volume is entirely managed by Docker. Volumes have several advantages over bind mounts, such as easier backup and migration, and are the preferred mechanism for persisting data generated by and used by Docker containers.

Objective:
Modify your existing Dockerfile to include a specified volume at /data. Demonstrate the persistence of data in this volume by:

Writing data to the volume.
Stopping the container.
Restarting the container.
Reading the data back from the volume to confirm its persistence.
Resources:
Docker Volumes documentation: https://docs.docker.com/storage/volumes/
