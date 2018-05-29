import json
import requests

GRAYLOG_API_URL = "http://{}:{}"
SEARCH_HANDLER = "/search"
SEARCH_ABSOLUTE_HANDLER = "{}/universal/absolute".format(SEARCH_HANDLER)
GET_FIELDS_HANDLER = "/system/fields"
FIELD_HANDLER = "&fields="
FILTER_HANDLER = "&filter="
STREAM_FILTER_HANDLER = "{}streams:".format(FILTER_HANDLER)

MESSAGE_NUM_LIMIT = 10000

GRAYLOG_API_TIME_STR_FORMAT = '%Y-%m-%d %H:%M:%S'

class GrayLogClient(object):
    def __init__(self, host, port, api_handleler, api_token):
        self.host = host
        self.port = port
        self.url = GRAYLOG_API_URL.format(host, port)
        self.api_handleler = api_handleler
        self.api_token = api_token

    def search(self, query, start_date, end_date, fields, streams):
        start_date_str = start_date.strftime(GRAYLOG_API_TIME_STR_FORMAT)
        end_date_str = end_date.strftime(GRAYLOG_API_TIME_STR_FORMAT)

        field_url = "{}{}".format(FIELD_HANDLER, ",".join(fields))
        streams_filter_url = "{}{}".format(STREAM_FILTER_HANDLER, ",".join(streams)) 

        search_url = "{}{}{}?query={}&limit={}&timestamp=asc&from={}&to={}{}{}".format(
            self.url, 
            self.api_handleler, 
            SEARCH_ABSOLUTE_HANDLER, 
            query, 
            MESSAGE_NUM_LIMIT, 
            start_date_str, 
            end_date_str, 
            field_url, 
            streams_filter_url)

        res = requests.get(search_url, auth=(self.api_token, 'token'))
        return json.loads(res.text)

    def get_fields(self):
        get_field_url = "{}{}{}".format(self.url, self.api_handleler, GET_FIELDS_HANDLER)

        res = requests.get(get_field_url, auth=(self.api_token, 'token'))
        return json.loads(res.text)
