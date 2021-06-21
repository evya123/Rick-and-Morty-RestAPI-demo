docker build . -t rnm
docker tag rnm kubernetes.docker.internal:44747/ex:1.0.0
docker push kubernetes.docker.internal:44747/ex:1.0.0