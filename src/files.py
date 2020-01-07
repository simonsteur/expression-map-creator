"""files module, deals with loading articulations file"""
#import os
import glob
import yaml

def readArticulationsFromFile(file):
    """reads in articulations yaml file"""
    try:
        articulations = yaml.safe_load(open(file, 'r'))
        return articulations
    except Exception as error:
        raise error

def readArticulationsFromDir(path):
    """reads in all articulation yaml files from directory"""
    try:
        searchDir = path + "/*.yaml"
        files = list()
        for file in glob.glob(searchDir):
            files.append(file)
        return files
    except Exception as error:
        raise error
