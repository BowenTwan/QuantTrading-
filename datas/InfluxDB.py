'''
This script is used to load A stock histotial data to InfluxDB.
Before runing this script, initalization of lcoal influxDB is required.
'''


from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

import pandas as pd

# initial client 
# You can generate a Token from the "Tokens Tab" in the UI
token = "UhksRgsTI7TvbxminGQsS9XdEOuq4HTuYZ3rZbmHBwhOb1cy65Pwjm1QwICYp1Tz39LVA1KveTPe-e3BwIuCfw=="
org = "TB"
bucket = "AStock"

client = InfluxDBClient(url="http://localhost:8086", token=token)


# write data 
write_api = client.write_api(write_options=SYNCHRONOUS)

# data = "mem,host=host1 used_percent=23.43234543"
data = pd.read_csv('/Users/bowenduan/Applications/OneDrive/200_Knowledge/270_Stock/QT/QuantTrading-/datas/AstockDailyData/StockList.csv')

write_api.write(bucket, org, data,data_frame_measurement_name='cpu')

# Execute query
query = f'from(bucket: \\"{bucket}\\") |> range(start: -1h)'
tables = client.query_api().query(query, org=org)