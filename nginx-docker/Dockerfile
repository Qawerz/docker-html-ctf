# Dockerfile.web
FROM nginx:alpine

RUN apk add --no-cache bash

# Create a simple HTML page that shows container ID
RUN echo -e '#!/bin/bash\n\necho "<!DOCTYPE html>\n<html>\n<head>\n<title>CTF Challenge</title>\n<style>\nbody { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }\n.container-id { font-size: 24px; color: #d9534f; margin: 20px; }\n</style>\n</head>\n<body>\n<h1>Web Challenge</h1>\n<p>Your container ID is:</p>\n<div class=\"container-id\">$(hostname)</div>\n<p>Find the flag hidden somewhere in this container!</p>\n</body>\n</html>" > /usr/share/nginx/html/index.html\n\nnginx -g "daemon off;"' > /start.sh

RUN chmod +x /start.sh

CMD ["/start.sh"]