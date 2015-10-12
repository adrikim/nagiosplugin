#!/usr/bin/env python
import sys, urllib2, json # argparse- different urls?

url = 'http://es-cluster.engin.umich.edu:9200/_cluster/health'
info = json.loads(urllib2.urlopen(url).read())

#print json.dumps(info)

