#!/usr/bin/env python3

import json
import sys
import argparse
import configparser

cf = configparser.ConfigParser()

cf.read('config_check.py')

java_comm = cf.get('java_service')

print(java_comm)

'''
configfile = open('config_check.py')
jsonconfig = json.load(configfile)
configfile.close()

jsonconfig
'''