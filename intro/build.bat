docker run --rm -v "%CD%:/out" node:25-alpine /bin/ash -c "npm install -g cleaver && cleaver /out/docker-vs-compose.md --output /out/docker-vs-compose.html"
