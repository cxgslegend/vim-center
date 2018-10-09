import json
import urllib.request
import vim
from IpInfo import IpInfo
from Line import Line

def print_info():
    ipInfo = IpInfo()
    print(ipInfo)

def center_text():
    line = Line()
    line.center_line()

def center_text_of_length(width):
    line = Line()
    line.center_line_of_length(width)

# In python eval(":w") will evaluate a vim expression


# vim.current.buffer.append('I was added by a Python plugin!') this is how you change or look at text in python







