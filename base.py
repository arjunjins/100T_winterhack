'''
02-12-2022
WINTER HACK - FOCUS WEB APP

Aromal Pradeep
Arjun Jins
Adithya Kartha
Alan George Mathews
'''

# IMPORTS
from flask import Flask

# FLASK


app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

if __name__ == '__main__':
   app.run()