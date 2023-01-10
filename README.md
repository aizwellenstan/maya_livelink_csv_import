```
import sys

sys.path.append(r'D:\workspace\td\lts\livelinkCsvImport')

import livelinkCsvImport
reload(livelinkCsvImport)
# Csv Path
facialPath = r'J:\test_project\work\progress\mcp\20221219'
rigFile = r'J:\test_project\work\progress\mcp\satou\facial\rig\kaikai.mb'
outPutPath = r'J:\test_project\work\progress\mcp\20221222\output'
livelinkCsvImport.insertKey(facialPath, rigFile, outPutPath)
```