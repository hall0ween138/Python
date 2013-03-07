import urllib2
import urllib
import time
import random

##start = time.time()
##for x in range(3):
##    print "Send hit..."
##    time.sleep(0)
##    r = urllib2.urlopen("http://statse.webtrendslive.com/dcsehhbtsvz5bdiav0m1b8akn_2m2n/dcs.gif?dcsredirect=126&test=test&test=test1&dcstlh=0&dcstlv=0&dcsdat=1348249393901&dcssip=us.asos.com&dcsuri=/Shop-mens-clothes-jeans-shoes-t-shirts-shirts-and-more-at-ASOS/wvo3u/&dcsqry=?r=1%26mk=VOID&WT.tz=-7&WT.bh=10&WT.ul=en-US&WT.cd=32&WT.sr=1920x1080&WT.jo=Yes&WT.ti=Shop%20men%u2019s%20clothes%2c%20jeans%2c%20shoes%2c%20t-shirts%2c%20shirts%20and%20more%20at%20ASOS&WT.js=Yes&WT.jv=1.5&WT.ct=unknown&WT.bs=1856x122&WT.fv=11.3&WT.slv=Unknown&WT.tv=9.3.0&WT.sp=ASOS%20US&WT.dl=0&WT.ssl=0&WT.es=us.asos.com/Shop-mens-clothes-jeans-shoes-t-shirts-shirts-and-more-at-ASOS/wvo3u/&WT.si_n=htob&WT.si_x=2&WT.cg_n=men&WT.vt_f_tlh=1348249380&WT.vtvs=1348249380637&WT.vtid=216.64.169.240-76086432.30234958&WT.co_f=216.64.169.240-76086432.30234958&country=US&pType=Floor%20Page&content=men&wt.tcc=foo")
##elapsedTime = (time.time() - start)
##print elapsedTime

start = time.time()
count = 0
for x in range(500):
    time.sleep(1)
    #url = 'http://lscs.staging.dmz/dcscdq79k10000ws33akfryho_9g9w/dcs.gif?WT.ti=OPS_TEST'
    url = 'http://lscs.staging.dmz/dcssxsv6uqy4tg0g5jmichwud_7z8e/dcs.gif?WT.ti=QA_TEST&WT.cg_n=hello%20world'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    req = urllib2.Request(url, "", headers)
    response = urllib2.urlopen(req)
    the_page = response.read()
    print "Request"+str(count)
    count = count+1
elapsedTime = (time.time() - start)
print elapsedTime