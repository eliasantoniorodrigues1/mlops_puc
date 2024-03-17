from fastapi import FastAPI

app = FastAPI(title='Fetal Health API',
              openapi_tags=[
                  {
                  'name': '',
                  'description': '',
                  },
                  {
                    'name': '',
                    'description': ''
                    }])


# to run fasapi: uvicorn api.main:app -- reload
@app.get(path='/')
def home():
    return {'status': 'healthy'}
