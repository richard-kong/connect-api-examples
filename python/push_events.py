# -*- coding: utf-8 -*-
from requests_futures.sessions import FuturesSession
import json

#replace with "project id" get from app.getconnect.io
project_id = "PROJECT_ID"

#replace with "push key" for your project get from app.getconnect.io
api_key = "PUSH_KEY"

base_url = "https://api.getconnect.io"

connect = FuturesSession()
connect.headers.update({"Content-Type": "application/json", "X-Api-Key": api_key, "X-Project-Id": project_id})

def post_event(collection_name, event):
    """ Post a single event to Connect API async.
   
    :param event: dict object with the event data to push to connect
    :param collection_name: name of the collection for the event
    """
    
    url = "{0}/events/{1}".format(base_url, collection_name)
    payload = json.dumps(event)
    print "Pushing event..."
    connect.post(url = url, data = payload)       
    print "Pushing event complete"
    
def post_events(collection_name, events):
   """ Post multiple events to the Connect API as a batch

    returns list of dicts indicating success/failure of each event
    
   :param events: list of events as dicts
   :param collection_name: name of the collection for the event
   """
   
   url = "{0}/events".format(base_url)
   event_batch = {collection_name : events}
   payload = json.dumps(event_batch)
   print "Pushing event batch..."
   r = connect.post(url = url, data = payload)       
   
   #wait for response - to push async remove r.result()
   response  = r.result()
   print "Pushing event batch complete"
   print response
   results = response.json()
       
   return results
   
   
    
if __name__ == '__main__':
    single_event = {
        'type': 'cycling',
        'distance': 21255,
        'caloriesBurned': 455,
        'duration': 67,
        'user': {
            'id': '638396',
            'name': 'Bruce'
            }
        }
        
    post_event("my_collection_1",single_event)
    
    
    multi_events = [{
      'type': 'cycling',
      'distance': 21255,
      'caloriesBurned': 455,
      'duration': 67,
      'user': {
        'id': '638396',
        'name': 'Bruce'
      }
    },
    {
      'type': 'swimming',
      'distance': 21255,
      'caloriesBurned': 455,
      'duration': 67,
      'user': {
        'id': '638396',
        'name': 'Bruce',
      }
    }]
    
    results = post_events("my_collection_2",multi_events)
    
    print results
    
        
        