```
import sys

sys.path.append(r'D:\workspace\td\lts\livelinkCsvImport')

import livelinkCsvImport
reload(livelinkCsvImport)
# Csv Path
facialPath = r'facialPath'
rigFile = r'rigPath'
outPutPath = r'outPutPath'
livelinkCsvImport.insertKey(facialPath, rigFile, outPutPath)
```