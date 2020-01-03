"""arguments module, supplies argparse functionality"""
import argparse

parser = argparse.ArgumentParser(description=None)
parser.add_argument('--articulations', dest='articulations', default='', type=str, help='path to articulations file to create expression map from', required=True)
args = parser.parse_args()
