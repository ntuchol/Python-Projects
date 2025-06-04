@task
def extract(endpoint:str):
 # Sends GET request to an endpoint
 r = requests.get(endpoint) 

 return r.json()   # returns response as json
 @flow
def etl_pipeline():
   # Calls tasks in desired order
   json     = extract(ENDPOINT)  # Task 1
   df       = transform(json)    # Task 2
   response = load(df)           # Task 3

if __name__ == "__main__":
   etl_pipeline()