# GrayLog-Client

## Usage

`GC = GrayLogClient("localhost", 9000, "/api", "your_api_token")`

`fields = GC.get_fields()`

`search_results = GC.search_result_json(query='*', _from='2018-01-25 08:00:00', _to='2018-01-25 08:01:00', fields=fields["fields"])`

`search_results = GC.search_result_json(query='*', _from='2018-01-25 08:00:00', _to='2018-01-25 08:01:00', fields=["example_field_0", "example_field_1"])`

`search_results = GC.search_result_json(query='*', _from='2018-01-25 08:00:00', _to='2018-01-25 08:01:00', fields=fields["fields"], streams=["example_stream_ID_0", "example_stream_ID_1"])`
