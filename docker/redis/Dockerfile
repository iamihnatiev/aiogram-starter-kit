# Use the official Redis image from Docker Hub
FROM redis:latest

# Copy custom Redis configuration file into the container
COPY redis.conf /usr/local/etc/redis/redis.conf

# Specify the custom configuration file when starting Redis
CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]
