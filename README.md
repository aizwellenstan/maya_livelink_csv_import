```
import sys

sys.path.append(r'I:\script\bin\td\maya\scripts\mocapConvert')

import livelinkCsvImport
reload(livelinkCsvImport)

# Csv Path
facialPath = 'T:/mocap/work/prod/mcp/Facial'
rigFile = 'rig.fbx'
outPutPath = 'output_folder'
livelinkCsvImport.insertKey(facialPath, rigFile, outPutPath)
```