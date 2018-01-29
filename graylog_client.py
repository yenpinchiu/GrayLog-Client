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

        url = "{}{}{}?query={}&from={}&to={}{}{}".format(self.url,
         self.api_handleler, SEARCH_ABSOLUTE_HANDLER, query,
          _from, _to, field_url, streams_filter_url)

        res = requests.get(url, auth=(self.api_token, 'token'))
        return res

    def search_parsed_result(self, query, _from, _to, fields, streams=None):
        res = self.search(query, _from, _to, fields, streams)
        log_strs = res.text.split("\n")

        result = []
        first_element_flag = True
        for log_str in log_strs:
            log_str_split = log_str.split(",")
            
            log_str_split = [ log[1:-1] for log in log_str_split]

            if first_element_flag:
                keys = log_str_split
                first_element_flag = False
                continue

            log_json = {}
            for i, (key, log) in enumerate(zip(keys, log_str_split)):
                log_json.update({key:log})

            result.append(log_json)

        return result

    def get_fields(self):
        url = "{}{}{}".format(self.url, self.api_handleler, GET_FIELDS_HANDLER)

        res = requests.get(url, auth=(self.api_token, 'token'))
        return json.loads(res.text)
