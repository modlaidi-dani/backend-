import os
import multiprocessing
workers = 3
chdir = "/home/afifa/ERP/erpdivatech"
bind = '0.0.0.0:8000'
wsgi_app = "erpdivatech.wsgi:application"
timeout = 300

