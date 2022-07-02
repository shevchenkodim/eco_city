FROM nginx:1.19.7-alpine
COPY proxy/nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]