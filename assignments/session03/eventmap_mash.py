__author__ = 'brianschmitz'




import eventful

api = eventful.API('test_key', cache='.cache')
# api.login('username', 'password')
events = api.call('/events/search', q='running', l='Seattle', )

for event in events['events']['event']:
    print "%s at %s" % (event['title'], event['venue_name'],)
    print event['start_time']
    print event['description']

import requests

URL = 'https://www.google.com/search?pz=1&cf=all&ned=us&hl=en&tbm=nws&gl=us&as_q={query}&as_occt=any&as_drrb=b&as_mindate={month}%2F%{from_day}%2F{year}&as_maxdate={month}%2F{to_day}%2F{year}&tbs=cdr%3A1%2Ccd_min%3A3%2F1%2F13%2Ccd_max%3A3%2F2%2F13&as_nsrc=Gulf%20Times&authuser=0'


def run(**params):
    response = requests.get(URL.format(**params))
    print response.content, response.status_code


# run(query=event['description'], month=1, from_day=1, to_day=1, year=14)

# -*- coding: utf-8 -*-
import urllib
import urllib2
import json

def main(event):
    query = event
    print bing_search(query, 'Web')
    # print bing_search(query, 'Image')

def bing_search(query, search_type):
    #search_type: Web, Image, News, Video
    key= 'fIXP2iI8QV2pPFpJBao3e5lfrMP8B27CtQ5c2UkKq3w'
    query = urllib.quote(query)
    # create credential for authentication
    user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)'
    credentials = (':%s' % key).encode('base64')[:-1]
    auth = 'Basic %s' % credentials
    url = 'https://api.datamarket.azure.com/Data.ashx/Bing/Search/'+search_type+'?Query=%27'+query+'%27&$top=5&$format=json'
    request = urllib2.Request(url)
    request.add_header('Authorization', auth)
    request.add_header('User-Agent', user_agent)
    request_opener = urllib2.build_opener()
    response = request_opener.open(request)
    response_data = response.read()
    json_result = json.loads(response_data)
    result_list = json_result['d']['results']
    print result_list
    return result_list

if __name__ == "__main__":
    main(event['description'])