import json
import requests

GRAYLOG_API_URL = "http://{}:{}"
SEARCH_HANDLER = "/search"
SEARCH_ABSOLUTE_HANDLER = "{}/universal/absolute".format(SEARCH_HANDLER)
GET_FIELDS_HANDLER = "/system/fields"
FIELD_HANDLER = "&fields="
FILTER_HANDLER = "&filter="
STREAM_FILTER_HANDLER = "{}streams:".format(FILTER_HANDLER)

class GrayLogClient(object):
    def __init__(self, host, port, api_handleler, api_token):
        self.host = host
        self.port = port
        self.url = GRAYLOG_API_URL.format(host, port)
        self.api_handleler = api_handleler
        self.api_token = api_token

    def search(self, query, _from, _to, fields, streams=None):
        field_url = "{}{}".format(FIELD_HANDLER, ",".join(fields))

        if streams is None:
            streams_filter_url = ""
        else:
            streams_filter_url = "{}{}".format(STREAM_FILTER_HANDLER, ",".join(streams)) 

        search_url = "{}{}{}?query={}&from={}&to={}{}{}".format(self.url,
         self.api_handleler, SEARCH_ABSOLUTE_HANDLER, query,
          _from, _to, field_url, streams_filter_url)

        res = requests.get(search_url, auth=(self.api_token, 'token'))
        return res

    def search_result_json(self, query, _from, _to, fields, streams=None):
        res = self.search(query, _from, _to, fields, streams)
        res_text = res.text
        res_text_json = json.loads(res_text)

        return res_text_json

    def get_fields(self):
        get_field_url = "{}{}{}".format(self.url, self.api_handleler, GET_FIELDS_HANDLER)

        res = requests.get(get_field_url, auth=(self.api_token, 'token'))
        return json.loads(res.text)
