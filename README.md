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

message_num_limit = 100

# if stream and fields not set, in default it will search on all stream and return all field of each messages
search_results = GC.search(
    query='*', 
    start_date=start_time, 
    end_date=end_time, 
    message_num_limit)

# multiple stream search not supported currently
search_results = GC.search(
    query='*', 
    start_date=start_time, 
    end_date=end_time, 
    message_num_limit, 
    stream=test_stream_0)

search_results = GC.search(
    query='*', 
    start_date=start_time, 
    end_date=end_time, 
    message_num_limit, 
    fields=[test_field_0, test_field_1])

for message in search_results['messages']:
    print(message)
```
