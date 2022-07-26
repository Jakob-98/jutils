import sys, os, argparse, yaml

parser = argparse.ArgumentParser(description='Configure a jconfig')
parser.add_argument('-c', '--config', help='Config .yaml file path', type=str, default='./config.yaml')
args = parser.parse_args()

# Load config file
with open(args.config, 'r') as f:
    configyaml = yaml.load(f, Loader=yaml.FullLoader)

class config:
    for key, value in configyaml.items():
        locals()[key] = value
