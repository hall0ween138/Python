import httplib2
import json
from pprint import pprint
from xml.etree import ElementTree
import sys
from optparse import OptionParser
 
# Arg parser for command line arguments
parser = OptionParser()
parser.add_option("-r","--role", dest="lf_dest", help="Enter the role list file location", metavar="ROLE LIST FILE")
parser.add_option("-e","--env",dest="env_file", help="Enter the environment file location", metavar="ENVIRONMENT FILE")
(options, args) = parser.parse_args()
 
# Uncomment to run interactive mode
#lf_dest = raw_input("Enter the ROLELIST.JSON  file location >>> ")
#env_file = raw_input("Enter the ENVIRONMENT.JSON file location >>> ")
 
# Function to replace key value in dict
def fixup(adict, k, v):
   for key in adict.keys():
       if key == k:
           adict[key] = v
       elif type(adict[key]) is dict:
           fixup(adict[key], k, v)
 
# Open role list file
try:
        list_file = open(options.lf_dest)
except IOError:
        print "Cannot open the roles list file either because of an error or the file does not exist"
        sys.exit()
except TypeError:
        print '''Please supply valid arguments when running EnvCopy - Use "Python EnvCopy.py --help" to get a full list'''
        sys.exit()
except NameError:
        print '''Please supply valid arguments when running EnvCopy - Use "Python EnvCopy.py --help" to get a full list'''
        sys.exit()
 
# Deserialize json in list file 
try:
        list_json_load = json.load(list_file)
except NameError:
        print "Could not load roles list file as json"
 
# Open env file
try:
        json_data=open(options.env_file)
except IOError:
        print "Cannot open the file either because of an error or the file does not exist"
        sys.exit()
 
# Deserialize json in env file
try:
        data = json.load(json_data)
except NameError:
        print "Could not load roles list file as json"
 
# TBFL
for each in list_json_load:
        role_name = each
        print '''
        '''
        print ">>> You will now be updating "+role_name
 
# Check that the file will work based on the existence of default_attributes
        if 'default_attributes' in data:
                pass
        else:
                print ">>> The environment file does not have any default attributes"
 
# Map role to bt number
        bt_dict = {
        "hadoop": "na",
        "hbase": "na",
       "hive": "na",
       "iis": "na",
       "java": "na",
       "kafka": "na",
       "nagios": "na",
       "nginx": "na",
       "storm": "na",
       "ubuntu": "na",
       "webpi": "na",
       "webtrends_server": "na",
       "windows": "na",
       "wt_base": "na",
       "wt_cam": "bt324",
       "wt_kafka_topagg": "bt307",
       "wt_netacuity": "na",
       "wt_portfolio_admin": "bt239",
       "wt_portfolio_manager": "bt294",
       "wt_publishver": "na",
       "wt_realtime_hadoop": "na",
       "wt_sauth": "bt324",
       "wt_storm_streaming": "bt249",
       "wt_streaming_viz": "bt241",
       "wt_streaminganalysis_monitor": "bt300",
       "wt_streamingapi": "bt244",
       "wt_streamingauditor": "bt246",
       "wt_streamingconfigservice": "bt247",
       "wt_streaminglogreplayer": "bt248",
       "wt_streamingmanagementservice": "bt327",
       "zookeeper": "na"}
 
        if role_name==role_name:
                bt_number=bt_dict[role_name]
 
# Map role to artifact zip name
        zip_dict = {
        "hadoop": "na",
       "hbase": "na",
       "hive": "na",
       "iis": "na",
       "java": "na",
       "kafka": "na",
       "nagios": "na",
       "nginx": "na",
       "storm": "na",
       "ubuntu": "na",
       "webpi": "na",
       "webtrends_server": "na",
       "windows": "na",
       "wt_base": "na",
       "wt_cam": "CAM.zip",
       "wt_kafka_topagg": "TopicAggregator-bin.tar.gz",
       "wt_netacuity": "na",
       "wt_portfolio_admin": "Portfolio.Admin.zip",
       "wt_portfolio_manager": "Portfolio.Manager.zip",
       "wt_publishver": "na",
       "wt_realtime_hadoop": "na",
       "wt_sauth": "auth.zip",
       "wt_storm_streaming": "streaming-analysis-bin.tar.gz",
       "wt_streaming_viz": "Streaming.Viz.zip",
       "wt_streaminganalysis_monitor": "webtrends-streaming-analysis-monitor-bin.tar.gz",
       "wt_streamingapi": "webtrends-streamingapi-bin.tar.gz",
       "wt_streamingauditor": "webtrends-streamingauditor-bin.tar.gz",
       "wt_streamingconfigservice": "webtrends-streaming-configservice-bin.tar.gz",
       "wt_streaminglogreplayer": "webtrends-streaminglogreplayer-bin.tar.gz",
       "wt_streamingmanagementservice": "webtrends-streaming-managementservice-bin.tar.gz",
       "zookeeper": "na"}
 
        if role_name==role_name:
                build_artifact_zip=zip_dict[role_name]
 
# Create the TC request to obtain build number based on bt number and build tag
        buildinfo_url = "http://teamcity.webtrends.corp/guestAuth/app/rest/builds/?locator=buildType:%s,tags:%s,branch:branched:any" % (bt_number, list_json_load[role_name][0]['tag'])
 
# Send HTTP GET request to TC to get the build id
        client = httplib2.Http()
        response, xml = client.request(buildinfo_url)
 
# Extract the build id from the response xml
        doc = ElementTree.fromstring(xml)
        if role_name=="wt_cam": 
                for id in doc.findall('build'):
                        build_id = "%s" % (id.attrib['id'])
                try:
                        download_url = "http://teamcity.webtrends.corp/guestAuth/repository/download/%s/%s:id/%s" % (bt_number, build_id, build_artifact_zip)
                       fixup(data, 'download_url', download_url)               
                except NameError:
                        print "No build exists with that tag or could not find build with specified tag"
        else:
                for id in doc.findall('build'):
                         build_id = "%s" % (id.attrib['id'])
               try:
                       download_url = "http://teamcity.webtrends.corp/guestAuth/repository/download/%s/%s:id/%s" % (bt_number, build_id, build_artifact_zip)
                        data["default_attributes"][role_name]["download_url"] = download_url
               except NameError:
                       print "No build exists with that tag or could not find build with specified tag"
 
# Show the new download url
       print ">>> Here is the new download_url: "+download_url
 
# Create a tmp file to dump the new JSON into - then we will delete the original and rename the tmp file to the original
       tmp_file = open(options.env_file,'w')
       json.dump(data, tmp_file, sort_keys=True, indent=4)
 
# Close the JSON file now that we are done with it
        tmp_file.close()
        
# Close json_data file since we don't use it anymore
json_data.close()
 
# Close the role list file
list_file.close()