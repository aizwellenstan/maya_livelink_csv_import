import csv
import maya.cmds as cmds
import sys
import os
from os import listdir
from os.path import isfile, join
import pymel.core as pm
from fbxExport import FBXExportMelEval

def add_path(path):
    if path not in sys.path:
        sys.path.insert(0, path)
python_version = '%d.%d' % sys.version_info[:2]

def set_playback_range_to_fit_keyframes():
    pm.playbackOptions(minTime=start_frame)
    pm.playbackOptions(maxTime=end_frame)

def cleanData(data):
    newData = []
    lastTimeCode = 0
    lastData = []
    for d in data:
        if len(d) < 1: continue
        timeCode = int(d[0][-3:])
        if d[1] == "0": continue
        if lastTimeCode > 0:
            if timeCode - lastTimeCode > 1:
                for i in range(0, timeCode - lastTimeCode):
                    newData.append(lastData)
        newData.append(d)
        lastData = d
        lastTimeCode = timeCode
    return newData
    
def createAnimationArr(header, data):
    animationArr = []
    for d in data:
        if len(d) < 3: continue
        dataDict = {}
        for i in range(2, 53):
            dataDict[header[i]] = float(d[i])
        animationArr.append(dataDict)
    return animationArr

def selectNurbsCurve(nurbsCurveName):
    curve_transforms = [cmds.listRelatives(i, p=1, type='transform')[0] for i
    in cmds.ls(type='nurbsCurve', o=1, r=1, ni=1)]
    for curve in curve_transforms:
        if nurbsCurveName == curve:
            return curve
    return ""

def setKeyframes(facialName, data):
    frame = 0
    for d in data:
        for key, val in d.items():
            key_lowercase = key[0].lower() + key[1:]
            cmds.setKeyframe(facialName+'.'+key_lowercase, value=val, time=frame)
        frame += 1

def getData(path):
    data = []
    with open(path) as f:
        reader = csv.reader(f)
        header = next(reader)
        data = [row for row in reader]
    return header, data

def setTimeLine():
    all = cmds.ls("*", long=True)
    cmds.select(all)
    all_keys = sorted(cmds.keyframe(all, q=True) or [])
    if all_keys:
        start = int(all_keys[0])
        end = int(all_keys[-1])
    print(start, end)
    cmds.playbackOptions(min=start, max=end)

def insertKey(facialPath, rigFile, outPutPath):
    excludeDir = 'livelinkFace'
    onlyfiles = []
    for path, subdirs, files in os.walk(facialPath):
        for name in files:
            if name.endswith('.csv'):
                if excludeDir in path: continue
                fpath = os.path.join(path, name)
                onlyfiles.append(fpath)

    # onlyfiles = [f for f in listdir(facialPath) if (isfile(join(facialPath, f)) and f.endswith('.csv'))]
    print(onlyfiles)
    facialName = 'Morpher'

    for f in onlyfiles:
        basename_without_ext = os.path.splitext(os.path.basename(f))[0]
        header, data = getData(f)
        data = cleanData(data)
        animationArr = createAnimationArr(header, data)
        fileName = os.path.splitext(f)[0]
        print(fileName)
        cmds.file(rigFile, open=True, force=True)
        setKeyframes(facialName, animationArr)
        setTimeLine()
        # cmds.file(rename=outPutPath+'/'+fileName+".ma")
        # cmds.file(save=True, type="mayaAscii")
        exportPath = outPutPath+'/'+basename_without_ext+'.fbx'.encode('unicode_escape')
        FBXExportMelEval(exportPath)