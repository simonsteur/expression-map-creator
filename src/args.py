"""arguments module, supplies argparse functionality"""
import argparse

parser = argparse.ArgumentParser(description=None)
parser.add_argument('--file', dest='file', default='', type=str, help='path to articulations file to create expression map from')
parser.add_argument('--dir', dest='dir', default='', type=str, help='path to directory containing yaml files to create expression maps from')
args = parser.parse_args()
