#********requests********#
import requests

response = requests.get('http://example.com/api/resource')

print(response.text)



#********httplib********#
import httplib

conn = httplib.HTTPConnection('example.com')
conn.request('GET', '/api/resource')

response = conn.getresponse()
print(response.read())



#********urllib********#
import urllib

response = urllib.urlopen('http://example.com/api/resource')
print(response.read())



#********aiohttp********#
import aiohttp
import asyncio

async with aiohttp.ClientSession() as session:
    async with session.get('http://example.com/api/resource') as response:
        print(await response.text())
        


#********pycurl********#
import pycurl

c = pycurl.Curl()
c.setopt(c.URL, 'http://example.com/api/resource')
c.perform()
print(c.response_code)
print(c.body)



#********httx********#
import httx

response = httx.get('http://example.com/api/resource')
print(response.status_code)
print(response.text)



#********http.client********#
import http.client

conn = http.client.HTTPSConnection('example.com')
conn.request('GET', '/api/resource')

response = conn.getresponse()
print(response.read())



#********treq********#
import treq

def print_response(response):
    print(response.code)
    print(response.headers)
    print(response.text())

treq.get('http://example.com/api/resource').addCallback(print_response)



#********grequests********#
import grequests

def print_response(response):
    print(response.status_code)
    print(response.headers)
    print(response.text)

rs = [grequests.get('http://example.com/api/resource')]
grequests.map(rs).addCallback(print_response)



#********httpx********#
import httpx

response = httpx.get('http://example.com/api/resource')
print(response.status_code)
print(response.headers)
print(response.text)



#********httptools********#
import httptools

def on_headers(headers):
    print(headers)

def on_body(body):
    print(body)

def on_response(response):
    print(response)

httptools.parse_url('http://example.com/api/resource', on_headers, on_body, on_response)



#********http_client********#
import http_client

response = http_client.get('http://example.com/api/resource')
print(response.status_code)
print(response.headers)
print(response.text)



#********requests_async********#
import requests_async

async def main():
    response = await requests_async.get('http://example.com/api/resource')
    print(response.status_code)
    print(response.headers)
    print(response.text)

await main()



#********httplib2********#
import httplib2

http = httplib2.Http()
response, content = http.request('http://example.com/api/resource', 'GET')
print(response.status)
print(content)



#********httplib3********#
import httplib3

http = httplib3.Http()
response = http.request('http://example.com/api/resource', 'GET')
print(response.status)
print(response.data)



#********httplib4********#
import httplib4

http = httplib4.Http()
response = http.request('http://example.com/api/resource', 'GET')
print(response.status)
print(response.data)



#********httptools2********#
import httptools2

def on_headers(headers):
    print(headers)

def on_body(body):
    print(body)

def on_response(response):
    print(response)

httptools2.parse_url('http://example.com/api/resource', on_headers, on_body, on_response)



#********http_client2********#
import http_client2

response = http_client2.get('http://example.com/api/resource')
print(response.status_code)
print(response.headers)
print(response.text)



#********requests_async2********#
import requests_async2

async def main():
    response = await requests_async2.get('http://example.com/api/resource')
    print(response.status_code)
    print(response.headers)
    print(response.text)

await main()



#********httplib5********#
import httplib5

http = httplib5.Http()
response, content = http.request('http://example.com/api/resource', 'GET')
print(response.status)
print(content)



#********httplib5********#
import httplib5

http = httplib5.Http()
response, content = http.request('http://example.com/api/resource', 'GET')
print(response.status)
print(content)