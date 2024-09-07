#!/usr/bin/env python3
import os
import re
import json
import sys

if __name__ == "__main__":
    data = {
        "runtimes": {}
    }
    for file in os.listdir(sys.argv[1]):
        m = re.match(r"(?P<name>.*)\.runtime\.(?P<RID>.*?)\.(?P<ver>.*)\.nupkg", file)
        if m is None: continue
        data['runtimes'][m.group("RID")] = {
            m.group("name") : {
                f'{m.group("name")}.runtime.{m.group("RID")}' : m.group("ver")
            }
            
        }
    print(json.dumps(data, indent=2, sort_keys=True))
