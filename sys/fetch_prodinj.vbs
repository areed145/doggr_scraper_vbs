Dim ArgObj
Dim api
Dim stream
Dim filesys
Set ArgObj=Wscript.Arguments
Set filesys = CreateObject("Scripting.FileSystemObject")
varPathCurrent = filesys.GetParentFolderName(WScript.ScriptFullName)
varPathParent = filesys.GetParentFolderName(varPathCurrent)

api=ArgObj.Item(1)
stream=ArgObj.Item(0)

' Set your settings
    strFileURL = "https://secure.conservation.ca.gov/WellSearch/Download/ToExcel" & stream & "Data?APInumber=" & api
    strHDLocation = varPathParent & "/wells/" & api & "_" & stream & ".xlsx"

' Fetch the file
    Set objXMLHTTP = CreateObject("MSXML2.XMLHTTP")

    objXMLHTTP.open "GET", strFileURL, false
    objXMLHTTP.send()

If objXMLHTTP.Status = 200 Then
Set objADOStream = CreateObject("ADODB.Stream")
objADOStream.Open
objADOStream.Type = 1 'adTypeBinary

objADOStream.Write objXMLHTTP.ResponseBody
objADOStream.Position = 0    'Set the stream position to the start

Set objFSO = Createobject("Scripting.FileSystemObject")
If objFSO.Fileexists(strHDLocation) Then objFSO.DeleteFile strHDLocation
Set objFSO = Nothing

objADOStream.SaveToFile strHDLocation
objADOStream.Close
Set objADOStream = Nothing
End if

Set objXMLHTTP = Nothing