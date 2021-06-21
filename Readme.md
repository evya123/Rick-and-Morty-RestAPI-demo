# RestAPI Rick and Morty

This repository contains a restapi application based on python 3.


# Running
### Prerequisitions
1. Docker installed.
2. Python3 installed.
3. Port 5000 is free.

In order to use this application:
##### Using docker standalone container:

    git clone
    cd <repository file>
    chmod +x run.sh
    ./run.sh
##### Using k8s deployment:
For an example I used k3d local cluster. [k3d site](https://k3d.io/).

    git clone
    cd Elementor
    chmod +x k8s.sh
    ./k8s.sh

## Changing configuration

To change the port, you need to edit run.sh - change port flag -p to <new_port>:5000
## Usage
#### Get all characters:
With postman simply query using get with url:

    http://localhost:5010/characters
Using python script:

    import requests
    session = requests.session()
    url = "http://localhost:5000/characters"
    res = session.get(url=url,verify=False)
    print(res.json())
##### Query parameters:
-   `name`: filter by the given name.
-   `status`: filter by the given status (`alive`,  `dead`  or  `unknown`).
-   `species`: filter by the given species.
-   `type`: filter by the given type.
-   `gender`: filter by the given gender (`female`,  `male`,  `genderless`  or  `unknown`).
##### Example:

    import requests
    session = requests.session()
    url = "http://localhost:5000/characters?name=rick&status=alive&origin=earth"
    res = session.get(url=url,verify=False)
    print(res.json())
respons:

    [
       {
          "Image_link":"https://rickandmortyapi.com/api/character/avatar/1.jpeg",
          "Location":"Earth (Replacement Dimension)",
          "Name":"Rick Sanchez"
       },
       {
          "Image_link":"https://rickandmortyapi.com/api/character/avatar/72.jpeg",
          "Location":"Citadel of Ricks",
          "Name":"Cool Rick"
       },
       {
          "Image_link":"https://rickandmortyapi.com/api/character/avatar/265.jpeg",
          "Location":"Earth (Replacement Dimension)",
          "Name":"Pickle Rick"
       },
       {
          "Image_link":"https://rickandmortyapi.com/api/character/avatar/288.jpeg",
          "Location":"Citadel of Ricks",
          "Name":"Rick D716-B"
       },
       {
          "Image_link":"https://rickandmortyapi.com/api/character/avatar/289.jpeg",
          "Location":"Citadel of Ricks",
          "Name":"Rick D716-C"
       },
       {
          "Image_link":"https://rickandmortyapi.com/api/character/avatar/291.jpeg",
          "Location":"Citadel of Ricks",
          "Name":"Rick J-22"
       },
       {
          "Image_link":"https://rickandmortyapi.com/api/character/avatar/292.jpeg",
          "Location":"Earth (Replacement Dimension)",
          "Name":"Rick K-22"
       }
    ]

## K8S Deployment

We need to create 3 yamls:
1.	Deployment yaml, containing the container.
2.	Service yaml, exposing the port to the outside world.
3.	Ingress yaml, redirecting to a backend containing the service.

In the deployment yaml, you need to edit the registry url and port with your own information and image name.

	  apiVersion: apps/v1
	  kind: Deployment
	  metadata:
	    name: flask
	    labels:
	      app: flask
	  spec:
	    replicas: 1
	    selector:
	      matchLabels:
	        app: flask
	    template:
	      metadata:
	        labels:
	          app: flask
	      spec:
	        containers:
	        - name: flask
	          image: k3d-dev-registry:44747/ex:1.0.0
	          ports:
	          - containerPort: 5000

In the service yaml, you need to add the right label to the selector so the service will be familiar with the deployment. Also port can be changed from any port the loadbalancer listen to (in my case it's 8080).

    apiVersion: v1
	kind: Service
	metadata:
	  name: flask
	  labels:
	    app: flask
	spec:
	  ports:
	  - port: 8080
	    targetPort: 5000
	    protocol: TCP
	    name: flask
	  selector:
	    app: flask
	  type: LoadBalancer
In the ingress yaml need to add the service name we created earlier and the port we specified. the ingress will redirect to the service using the cluster loadbalancer.

    apiVersion: networking.k8s.io/v1
	kind: Ingress
	metadata:
	  name: nginx
	  annotations:
	    ingress.kubernetes.io/ssl-redirect: "false"
	spec:
	  rules:
	  - http:
	      paths:
	      - path: /
	        pathType: Prefix
	        backend:
	          service:
	            name: flask
	            port:
	              number: 8080
