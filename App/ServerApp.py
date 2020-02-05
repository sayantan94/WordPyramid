'''
Created on Feb 5, 2020

@author: sayantan
'''
import sys

import collections
from flask import Flask
from flask_restplus import Resource, Api


app = Flask(__name__)
api = Api(app, version='1.0', title='Pyramid Check Service', 
          description='API to validate pyramid structure')             
ns = api.namespace('v1', 
                   description='Click here to expand the end-points !')


@ns.route('/checkPyramid/<string>', endpoint='checkPyramid')
@ns.doc(params={'string': 'String to validate if pyramid structure exists !'})
class PyramidCheck(Resource):           
    def get(self,string):
        counter = collections.Counter(string.strip())
        isPyramid = True
        seen = set()
        for char,count in counter.items():
            if not char or count in seen:
                isPyramid = False
                break
            else:
                seen.add(count)
                    
        return {'isPyramid':isPyramid}

if __name__ == '__main__':
    arg = sys.argv
    #print(1111,port)
    port = 5000
    if len(arg) > 1:
        port = arg[-1]
    app.run(port = port, debug=True)  