trap "npm run stop" INT

(girder serve) &

(nginx -p . -c scripts/nginx.conf) &

wait
