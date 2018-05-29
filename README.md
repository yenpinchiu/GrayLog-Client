# GrayLog-Client

## Usage

```
from datetime import datetime as dt

GRAYLOG_URL = "graylog_server_address"
GRAYLOG_PORT = 9000
GRAYLOG_API_TOKEN = "graylog_api_token"
GRAYLOG_API_TIME_STR_FORMAT = '%Y-%m-%d %H:%M:%S'

start_time = dt.strptime('2018-05-01 00:00:00', GRAYLOG_API_TIME_STR_FORMAT)
end_time = dt.strptime('2018-05-20 00:00:00', GRAYLOG_API_TIME_STR_FORMAT)

GC = GrayLogClient(
    GRAYLOG_URL, 
    GRAYLOG_PORT, 
    "/api", 
    GRAYLOG_API_TOKEN)

fields = GC.get_fields()
test_field_0 = fields["fields"][0]
test_field_1 = fields["fields"][1]

streams = GC.get_streams()
test_stream_0 = streams["streams"][0]["id"]

search_results = GC.search(
    query='*', 
    start_date=start_time, 
    end_date=end_time, 
    100)

search_results = GC.search(
    query='*', 
    start_date=start_time, 
    end_date=end_time, 
    100, 
    stream=test_stream_0)

search_results = GC.search(
    query='*', 
    start_date=start_time, 
    end_date=end_time, 
    100, 
    fields=[test_field_0, test_field_1])

for message in search_results['messages']:
    print(message)
```
