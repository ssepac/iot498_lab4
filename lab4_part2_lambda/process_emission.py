import json
import logging
import sys
 
import greengrasssdk
 
# Logging
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
 
# SDK Client
client = greengrasssdk.client("iot-data")
 
# Counter
vehicles = {}
def lambda_handler(event, context):
    global vehicles
    if event['vehicle_id'] in vehicles:
        vehicles[event['vehicle_id']] = max(vehicles[event['vehicle_id']], event['vehicle_CO2'])
    else:
        vehicles[event['vehicle_id']] = event['vehicle_CO2']
 
    client.publish(
        topic="emission/{}".format(event['vehicle_id']),
        payload=json.dumps(
            {"message": "Max CO2 emission from {} is {}".format(event['vehicle_id'], vehicles[event['vehicle_id']])}
        ),
    )
 
    return
