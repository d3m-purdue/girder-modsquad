trap "npm run stop" INT

(girder serve) &

(cd client; yarn start) &

(nginx -p . -c scripts/nginx.conf) &

wait
