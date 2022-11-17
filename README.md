# Lab 4

## basicDiscovery.py
basicDiscovery.py emulates a local device, and pushes data to the IoT cloud via the Greengrass core. Upon connecting to the core, it reads data from the CSV files in `vehicle_data` line-by-line, and publishes to a topic that is configured to trigger a Lambda (as seen in `lab4_part2_lambda/process_emission.py`). This Lambda function maintains a map of max CO2 emissions data for each vehicle. Upon processing the data, a topic is published to that the vehicle that triggered the lambda is subcribed to, so that the vehicle can receive the results of the Lambda function. 

An example command that runs basicDiscovery.py is below:

```
python3 basicDiscovery.py --endpoint <amazon iot endpoint> --rootCA AmazonRootCA1.pem --cert <id>-certificate.pem.crt --key <id>-private.pem.key --thingName <vehicle_id> --topic <your-topic-name> --data-path <path-to-vehicle-csv-data> --mode both
```

## Visualizations of emissions data

Please see the README.md in the `jupyter` folder for a copy of the Jupyter Notebook and associated code to generate each visualization of vehicle emissions data.