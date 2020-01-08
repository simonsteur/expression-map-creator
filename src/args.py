"""arguments module, supplies argparse functionality"""
import argparse

parser = argparse.ArgumentParser(description=None)
parser.add_argument('--file', dest='file', default='', type=str, help='path to articulations file to create expression map from')
parser.add_argument('--dir', dest='dir', default='', type=str, help='path to directory containing yaml files to create expression maps from')
parser.add_argument('--dest', dest='dest', default='.', type=str, help='path to directory to store expression maps in')

args = parser.parse_args()
