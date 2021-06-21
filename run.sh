docker build . -t rnm
docker image tag rnm ex:1.0.0
docker run -it -p 5000:5000 ex:1.0.0