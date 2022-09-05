from argparse import ArgumentParser
from flask import Flask

def create_app(secret:str):
    app = Flask(__name__)
    app.config['secret'] = secret
    print('Passed item: ', app.config['secret'])
    return app

if __name__ == '__main__':
  
  parser = ArgumentParser()
  parser.add_argument('-secret')
  args = parser.parse_args()
  app = create_app(secret=args.secret)
  app.run(host="0.0.0.0", port=5001)