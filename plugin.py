#!/usr/bin/env python
import sys, urllib2, json # argparse- different urls?

'''
We want a plugin that shows:
- okay when the cluster is green
- warns when it's yellow
- criticals when it's red or unresponsive.
It should also format other data in a way that's useful for further graphing.

It should report most of the data as perfdata. Definitely at least:
- number of nodes
- number of active and total shards
- pending actions
'''
# http://es-cluster.engin.umich.edu:9200/_stats/_shards?pretty=true
# http://es-cluster.engin.umich.edu:9200/_stats?pretty=true
url = 'http://es-cluster.engin.umich.edu:9200/_cluster/health'
info = json.loads(urllib2.urlopen(url).read())

# Get overall status
status = (0 if info["status"] == "green"
          else 1 if info["status"] == "yellow"
          else 2) # critical is either that or unresponsive

# Get perfdata #
# Node data
n_nodes = info["number_of_nodes"]
n_datanodes = info["number_of_data_nodes"]
# Shard data
n_primary_shards = info["active_primary_shards"]
n_total_shards = info["active_shards"] # Should be the same as total # shards
# Action data
n_pending_actions = info["number_of_pending_tasks"]

# Print out to stdout in Icinga plugin format
print "Status", ("OK" if status == 0
                 else "WARNING" if status == 1
                 else "CRITICAL"), "|",
print "n_nodes=" + str(n_nodes),
print "n_datanodes=" + str(n_datanodes),
print "n_primary_shards=" + str(n_primary_shards),
print "n_total_shards=" + str(n_total_shards),
print "n_pending_actions=" + str(n_pending_actions)

sys.exit(status)
