#!/usr/bin/env python
"""
get the status of jobs
"""
import subprocess
import sys
import time

RUNNING_STATUS = ["PENDING", "CONFIGURING", "COMPLETING", "RUNNING", "SUSPENDED"]
jobid = sys.argv[-1]

def get_status(jobid):
    output = str(subprocess.check_output("sacct -j %s --format State --noheader | head -1 | awk '{print $1}'" % jobid, shell=True).strip())

    if "COMPLETED" in output:
        return "success"
    elif any(r in output for r in RUNNING_STATUS):
        return "running"
    else:
        return "failed"

status = get_status(jobid)

# if failed status, maybe try again in a couple secs
if status == "failed":
    time.sleep(1)
    status = get_status(jobid)

print(status)
