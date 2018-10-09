import json
import urllib.request
import vim

class IpInfo:
    def __init__(self):
        self.ipinfo = json.loads(self.response('http://ipinfo.io/json'))

    def response(self, url):
        with urllib.request.urlopen(url) as response:
            return response.read()

    @property
    def ip(self):
        return self.ipinfo['ip']

    @property
    def hostname(self):
        return self.ipinfo['hostname']

    @property
    def city(self):
        return self.ipinfo['city']

    @property
    def region(self):
        return self.ipinfo['region']

    @property
    def country(self):
        return self.ipinfo['country']

    @property
    def loc(self):
        return self.ipinfo['loc']

    @property
    def postal(self):
        return self.ipinfo['postal']

    @property
    def phone(self):
        return self.ipinfo['phone']

    @property
    def org(self):
        return self.ipinfo['org']


    def __str__(self):
        formatString =  'Ip:           {}\n'
        formatString += 'Hostname:     {}\n'
        formatString += 'City:         {}\n'
        formatString += 'Region:       {}\n'
        formatString += 'Country:      {}\n'
        formatString += 'Loc:          {}\n'
        formatString += 'Postal:       {}\n'
        formatString += 'Phone:        {}\n'
        formatString += 'Org:          {}'
        return formatString.format(self.ip,
                self.hostname,
                self.city,
                self.region,
                self.country,
                self.loc,
                self.postal,
                self.phone,
                self.org)

