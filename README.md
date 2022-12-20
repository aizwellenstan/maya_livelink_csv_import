```
import sys

sys.path.append(r'D:\workspace\td\lts\livelinkCsvImport')

import livelinkCsvImport
reload(livelinkCsvImport)
# Csv Path
facialPath = r'J:\test_project\work\progress\mcp\20221219\TangTang_free_soul_t03'
rigFile = r'J:\test_project\work\progress\mcp\satou\facial\rig\kaikai.ma'
outPutPath = r'J:\test_project\work\progress\mcp\20221219\output'
livelinkCsvImport.insertKey(facialPath, rigFile, outPutPath)
```