import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import logging
import sys
import pandas as pd
requests.packages.urllib3.disable_warnings(InsecureRequestWarning) #Disable SSL warnings

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

class rickAndMortyApi:

    def __init__(self):
        self.__url_prefix = 'https://rickandmortyapi.com/api'

        self.__session = requests.session()
        self.__session.headers['Content-Type'] = 'application/json'
        self.__session.headers['Accept'] = 'application/json'
                    
    def __get_resource(self,url):
        logging.info(f"Requesting Page: {url}")
        try:
            res = self.__session.get(url=url,verify=False)
        except Exception as err:
            logging.error(f"Could not retrieve data due to error: {err}")
            sys.exit(1)
        return res.json()

    def getCharacter(self, name=None, status=None, species=None, charType=None, gender=None):
        url = self.__url_prefix + "/character"
        query_filter = []
        if name:
            query_filter.append({'name' : name})
        if status:
            if status in ['alive', 'dead', 'unknown']:
                query_filter.append({'status' : status})
            else:
                logging.error("Name attribute is incorrect. Available values are ['alive', 'dead', 'unknown']")
                sys.exit(1)
        if charType:
            query_filter.append({'type' : charType})
        if gender:
            if gender in ['female', 'male', 'genderless', 'unknown']:
                query_filter.append({'gender' : gender})
            else:
                logging.error("Gender attribute is incorrect. Available values are ['female', 'male', 'genderless', 'unknown']")
                sys.exit(1)
        if species:
            query_filter.append({'species' : species})
        if len(query_filter):
            url += '/?'
            first = True
            for filter_obj in query_filter:
                attr_name, attr = next(iter(filter_obj.items()))
                if first:
                    url += f"{attr_name}={attr}"
                    first = False
                else:
                    url += f"&{attr_name}={attr}"
        return self.__get_resource(url)['results']

    def filterByOrigin(self, result, origin):
        logging.info(f'Filtering with origin {origin}')
        res=[]
        for obj in result:
            try:
                if origin in obj['origin']['name']:
                    res.append({
                        'Name' : obj['name'],
                        'Location': obj['location']['name'],
                        'Image_link' : obj['image']
                    })
            except Exception as e:
                logging.error(f"Could not filter by origin due to {e}")
                sys.exit(1)
        return res

    def export(self, jsonF, name):
        try:
            df = pd.DataFrame(jsonF)
            df.to_csv(f"{name}.csv", index=False)
        except Exception as e:
            logging.error(f"Could not export to csv due to {e}")
            sys.exit(1)

    def liveness(self):
        logging.info("Checking livness")
        try:
            res = self.__session.get(url=self.__url_prefix,verify=False)
        except Exception as err:
            logging.error(f"Could not retrieve data due to error: {err}")
            sys.exit(1)
        return res.status_code