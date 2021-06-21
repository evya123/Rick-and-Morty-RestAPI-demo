from . import rickAndMortyApi
from flask_restful import Resource, Api
from flask import json, request
from healthcheck import HealthCheck
class Index(Resource):
    def get(self):
        return json.dumps({'info' : 'Elementor RestAPI task'}), 200

class GetCharacters(Resource):
    
    def parseArgs(self, args):
        return {
            'name' : args.get('name', None),
            'status' : args.get('status', None),
            'species' : args.get('species', None),
            'type' : args.get('type', None),
            'gender' : args.get('gender', None),
            'origin' : args.get('origin', None)
        }

    def get(self):
        args = self.parseArgs(request.args)
        rnm = rickAndMortyApi()
        characters = rnm.getCharacter(
            name=args['name'],
            status=args['status'],
            species=args['species'],
            charType=args['type'],
            gender=args['gender']
        )
        if args['origin']:
            return json.dumps(rnm.filterByOrigin(characters,args['origin'].capitalize())), 200
        return json.dumps(characters), 200

class HealthCheck(Resource):
    def get(self):
        rnm = rickAndMortyApi()
        return rnm.liveness()
