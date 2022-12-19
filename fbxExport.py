# -*- coding: utf-8 -*-
from maya import cmds 
import pymel.core as pm
import maya.mel as mel

PLUGIN = 'fbxmaya.mll'

def FBXExportMelEval(FullFilePath,selectBool=True):
    FullFilePath = FullFilePath.replace('\\', '/')
    mel.eval("FBXExportApplyConstantKeyReducer -v true")
    evalMelExport(FullFilePath,selectBool)
    sendCmd="end"
    return sendCmd
    
#import FBXWrapper as fw
def FBXWrapperssetting(FullFilePath):
    FBXWrapper.FBXExport("-f",FullFilePath,"-s")

def evalMelExport(FullFilePath,selectBool):
    selectSave=""
    if(selectBool==True):
        selectSave="-es"
    else:
        selectSave="-ea"
    evalstr='file -force -options "v=0;" -typ "FBX export" -pr '+selectSave+' "'+FullFilePath+'";'
    mel.eval(evalstr)

def PyMELExport(FullFilePath):
    pm.FBXExport("-f",FullFilePath+"_pymel_mel_FBXExport","-s")
    
def cmdsFBXExportSettingsExport(FullFilePath):
    cmds.FBXExport("-f",FullFilePath,"-s") #OK

def cmdFileExport(FullFilePath):
    cmds.file(FullFilePath+"_cmdfile", exportSelected=True, type="FBX export")