#!/bin/env python3

import yaml, sys

def parseDict(dictValue, prefix):
    for key, value in dictValue.items():
        parseYaml(value, f"{prefix}.{key}")

def parseList(listValue, prefix):
    for i, value in enumerate(listValue):
        parseYaml(value, f"{prefix}[{i}]")

def parseSimpleValue(simpleValue, prefix):
    print(prefix, "=", simpleValue)

def parseYaml(yamlValue, prefix):
    if isinstance(yamlValue, dict):
        parseDict(yamlValue, prefix)
    elif isinstance(yamlValue, list):
        parseList(yamlValue, prefix)
    else:
        parseSimpleValue(yamlValue, prefix)

# Main converting function
def convert(file):
    print(f"Converting {file}")
    prefix = ""
    with open(file) as f:
        yamlFile = yaml.safe_load(f)
        parseYaml(yamlFile, prefix)

# Entry Point
if __name__ == "__main__":
    if len(sys.argv) > 1:
        convert(sys.argv[1])