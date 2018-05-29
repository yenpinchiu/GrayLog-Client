import json
import requests

GRAYLOG_API_URL = "http://{}:{}"
SEARCH_HANDLER = "/search"
SEARCH_ABSOLUTE_HANDLER = "{}/universal/absolute".format(SEARCH_HANDLER)
GET_FIELDS_HANDLER = "/system/fields"
GET_STREAMS_HANDLER = "/streams"
FIELD_HANDLER = "&fields="
FILTER_HANDLER = "&filter="
STREAM_POSTFIX = "streams:"

GRAYLOG_API_TIME_STR_FORMAT = '%Y-%m-%d %H:%M:%S'

class GrayLogClient(object):
    def __init__(self, host, port, api_handleler, api_token):
        self.host = host
        self.port = port
        self.url = GRAYLOG_API_URL.format(host, port)
        self.api_handleler = api_handleler
        self.api_token = api_token

    def search(self, query, start_date, end_date, message_num_limit, fields = None, stream = None):
        start_date_str = start_date.strftime(GRAYLOG_API_TIME_STR_FORMAT)
        end_date_str = end_date.strftime(GRAYLOG_API_TIME_STR_FORMAT)

        field_url = ""
        if fields is not None:
            field_url = "{}{}".format(FIELD_HANDLER, ",".join(fields))
        
        stream_url = ""
        if stream is not None:
            stream_url = "{}{}{}".format(FILTER_HANDLER, STREAM_POSTFIX, stream) 

        search_url = "{}{}{}?query={}&limit={}&timestamp=asc&from={}&to={}{}{}".format(
            self.url, 
            self.api_handleler, 
            SEARCH_ABSOLUTE_HANDLER, 
            query, 
            message_num_limit, 
            start_date_str, 
            end_date_str, 
            field_url, 
            stream_url)

        res = requests.get(search_url, auth=(self.api_token, 'token'))
        return json.loads(res.text)

    def get_fields(self):
        get_field_url = "{}{}{}".format(self.url, self.api_handleler, GET_FIELDS_HANDLER)

        res = requests.get(get_field_url, auth=(self.api_token, 'token'))
        return json.loads(res.text)

    def get_streams(self):
        get_stream_url = "{}{}{}".format(self.url, self.api_handleler, GET_STREAMS_HANDLER)

        res = requests.get(get_stream_url, auth=(self.api_token, 'token'))
        return json.loads(res.text)
