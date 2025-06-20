# Dockerfile
FROM alpine:latest

RUN apk update && apk add --no-cache openssh sudo bash && \
    adduser -D user && echo "user:ctfpassword" | chpasswd && \
    # Set root password
    echo "root:rootpassword" | chpasswd && \
    mkdir /home/user/.ssh && chmod 700 /home/user/.ssh && \
    ssh-keygen -A && \
    # Allow root login with password for this example (not recommended for production)
    echo "PermitRootLogin yes" >> /etc/ssh/sshd_config && \
    echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config && \
    echo "Port 22" >> /etc/ssh/sshd_config && \
    echo "AllowUsers user root" >> /etc/ssh/sshd_config

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]