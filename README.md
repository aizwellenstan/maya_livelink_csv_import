```
import sys

sys.path.append(r'D:\workspace\td\lts\livelinkCsvImport')

import livelinkCsvImport
reload(livelinkCsvImport)
# Csv Path
facialPath = r'facialPath'
rigFile = r'J:\test_project\work\progress\mcp\satou\facial\rig\test.ma'
outPutPath = r'outputPath'
livelinkCsvImport.insertKey(facialPath, rigFile, outPutPath)
```