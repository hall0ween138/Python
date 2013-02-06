import httplib2
import json
from pprint import pprint
from xml.etree import ElementTree

#Open role list file
lf_dest = raw_input("Enter the ROLELIST.JSON  file location >>> ")
env_file = raw_input("Enter the ENVIRONMENT.JSON file location >>> ")

#Iterate through list_file and assign role_name and tag_name
list_file = open(lf_dest)
list_json_load = json.load(list_file)

for k in list_json_load:
    role_name = k
    print "You will now be updating "+role_name
    print '''
    '''
#Collect parameters to use in finding roles in the environment file and looking up the build in teamcity
#role_name = raw_input("What role do you want to update?: ")
#tag_name = raw_input("What is the build tag in teamcity associated with the build for this role?: ")
# Create the json object from the .json file
    try:
        json_data=open(env_file)
        data = json.load(json_data)
    except IOError:
        print "Cannot open the file"
#Check that the file will work based on the existence of default_attributes
    if 'default_attributes' in data:
        print "Here is the current download_url or list of urls"
        pprint(data["default_attributes"][role_name]["download_url"])
    else:
        print "The environment file does not have any default attributes"
    print "We will now update the download_url based on your input earlier..."

# Map role to bt number
    bt_dict = {"hadoop": "",
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
        "wt_portfolio_manager": "bt249",
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
        "wt_streamingmanamgementservice": "bt307",
        "zookeeper": "na"}

    if role_name==role_name:
        bt_number=bt_dict[role_name]
    print bt_dict[role_name]

#Map role to artifact zip name
    zip_dict = {"hadoop": "",
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
        "wt_cam": "Portfolio CAM",
        "wt_kafka_topagg": "Streaming-TopAgg",
        "wt_netacuity": "na",
        "wt_portfolio_admin": "Portfolio Admin",
        "wt_portfolio_manager": "Portfolio Manager",
        "wt_publishver": "na",
        "wt_realtime_hadoop": "na",
        "wt_sauth": "",
        "wt_storm_streaming": "Streaming-Analysis",
        "wt_streaming_viz": "Dataviz",
        "wt_streaminganalysis_monitor": "Streaming-Analysis-Monitor",
        "wt_streamingapi": "webtrends-streamingapi-bin.tar.gz",
        "wt_streamingauditor": "Streaming-Auditor",
        "wt_streamingconfigservice": "Streaming-Config",
        "wt_streaminglogreplayer": "Streaming-LogReplay",
        "wt_streamingmanamgementservice": "Streaming-ManagementService",
        "zookeeper": "na"}

    if role_name==role_name:
        build_artifact_zip=zip_dict[role_name]

#Create the TC request to obtain build number based on bt number and build tag
    buildinfo_url = "http://teamcity.webtrends.corp/guestAuth/app/rest/builds/?locator=buildType:%s,tags:%s" % (bt_number, list_json_load[role_name][0]['tag'])

#Send HTTP GET request to TC to get the build id
    client = httplib2.Http()
    response, xml = client.request(buildinfo_url)

#Extract the build id from the response xml
    doc = ElementTree.fromstring(xml)
    for id in doc.findall('build'):
        build_id = "%s" % (id.attrib['id'])

        download_url = "http://teamcity.webtrends.corp/guestAuth/repository/download/%s/%s:id/%s" % (bt_number, build_id, build_artifact_zip)
        data["default_attributes"][role_name]["download_url"] = download_url

#Show the new download url
        print '''
        '''
        print "Here is the new download_url"
        pprint(data["default_attributes"][role_name]["download_url"])

#Create a tmp file to dump the new JSON into - then we will delete the original and rename the tmp file to the original
        tmp_file = open(env_file,'w')
        json.dump(data, tmp_file, indent=4)

#Close the JSON file now that we are done with it
        tmp_file.close()

#Close json_data file since we don't use it anymore
    json_data.close()

#Close the role list file
    list_file.close()
