```
import sys

sys.path.append(r'D:\workspace\td\lts\livelinkCsvImport')

import livelinkCsvImport
reload(livelinkCsvImport)
# Csv Path
facialPath = r'J:\test_project\work\progress\mcp\20221219'
rigFile = r'rigFile'
outPutPath = r'J:\test_project\work\progress\mcp\20221219\output'
livelinkCsvImport.insertKey(facialPath, rigFile, outPutPath)
```