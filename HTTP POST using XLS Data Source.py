import urllib, urllib2, cookielib
import json
import random
import string, getpass
import pymssql, xlrd

# Variables for Auth / Login Info - Not Applicable at this time
##U_Nm = raw_input('Please enter your Username and press <ENTER> : ')
##U_Pw = getpass.getpass('Please enter your Password and press <ENTER> : ')

# Datasource / XLS to JSON object for POST Request
def xls_to_json():
    book = xlrd.open_workbook("C:\\Documents and Settings\\rsmith\\Desktop\\Shared\\5000address.xls")
    to_Json = []
    for sheet in book.sheets(): 
            for rowx in xrange(sheet.nrows): 
                to_Json.append(tuple(sheet.cell(rowx, colx).value 
                                for colx in xrange(sheet.ncols)))
    j_S = ({"FirstName":'Russ_Py2multi5',"LastName":'Post_Py2multi5',"MiddleName":'A',
            "Prefix":'',"Suffix":'',"Company":'Co_PyTest2Multi',
            "Street1": '%s',"Street2":'%s',"Street3":'',"City":'%s',
            "State":'%s',"Zip":'%s',"ZipAddOn":'%s',
            "CountryId":'203',"CountryCode":'US',"CountryName":'United States',
            "Province":'',"PostalCode":'',"Phone":'',"Email":''})
# Auth the User and store cookie in cookie jar
    U_Nm = 'corpad_0'
    U_Pw = 'password1'
    Auth_Usr = json.dumps({'username' : U_Nm, 'password' : U_Pw})
    S_cookie = cookielib.CookieJar()
    urlAgent = urllib2.build_opener(urllib2.HTTPCookieProcessor(S_cookie))
    urlAgent.open('https://cc-pow01-v.corp.stamps.com/webpostage/ajax/authenticateuser.aspx', Auth_Usr)

# HTTP POST Add Contact - Returns Content: RecordID, ErrorCode and ErrorDescription    
    count = 0
    for i in range(5):
        x = json.dumps(j_S) % to_Json[count]
        count = count+1
        y = str(x)
        print count
        print "Creating JSON Obj for AddContact.aspx with the following values:"'''
    ''' +\
    y
        try:
            addConUrl = urlAgent.open('https://cc-pow01-v.corp.stamps.com/addressbook/ajax/AddContact.aspx', y)
            contents = addConUrl.read()
        except urllib2.HTTPError, error:
            print "ERROR: ", error.read()
    
# HTTP GET Updated Content -- Looking For New ContactID Details - must add resp.read() to view content
    resp = urlAgent.open('https://cc-pow01-v.corp.stamps.com/addressbook/ajax/SearchContacts.aspx')
    
if __name__ == '__main__':
    xls_to_json()