# RestAPI Rick and Morty

This repository contains a restapi application based on python 3.


# Running
### Prerequisitions
1. Docker installed.
2. Python3 installed.
3. Port 5000 is free.

In order to use this application:

    git clone https://github.com/evya123/Elementor.git
    cd Elementor
    chmod +x run.sh
    ./run.sh

## Changing configuration

To change the port, you need to edit run.sh - change port flag -p to <new_port>:5000
## Usage
#### Get all characters:
With postman simply query using get with url:

    http://localhost:5000/characters
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
