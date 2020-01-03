"""articulations module, deals with loading articulations file"""
import yaml
from args import args

def readArticulationsFile():
    """reads in articulations yaml file defined by argparse"""
    print(args)
    try:
        articulations = yaml.safe_load(open(args.articulations, 'r'))
        return articulations
    except Exception as error:
        raise error
