#!/usr/bin/env python3
# adapted from https://github.com/Snakemake-Profiles/generic

import sys
from subprocess import Popen, PIPE
from pathlib import Path

from snakemake.utils import read_job_properties


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


jobscript = sys.argv[1]
job_properties = read_job_properties(jobscript)

# default paramters defined in cluster_spec (accessed via snakemake read_job_properties)
cluster_param = job_properties["cluster"]

if job_properties["type"] == "single":
    cluster_param['name'] = job_properties["rule"]
elif job_properties["type"] == "group":
    cluster_param['name'] = job_properties["groupid"]
else:
    raise NotImplementedError(f"Don't know what to do with job_properties['type']=={job_properties['type']}")


# use the memory, time and threads specified in a rule. If not specified use the cluster config
for res in ["mem_gb", "time", "threads"]:
    if res in job_properties["resources"]:
        cluster_param[res] = job_properties["resources"][res]
    if res in job_properties:
        cluster_param[res] = job_properties[res]


# construct command:
command = "sbatch --nodes=1 "
keymap = {
    "threads": "cpus-per-task",
    "mem_gb": "mem",
    "partition": "partition",
    "time": "time"
}

for key, slurmkey in keymap.items():
    if key in cluster_param:
        command += f"--{slurmkey} {cluster_param[key]}"
        if key == "mem_gb":
            command += "G"
        command += " "

# log all the slurm files to a dir to not clutter everything
slurm_log_dir = "seq2science_slurm"
Path(slurm_log_dir).mkdir(exist_ok=True)
command += f"--error={slurm_log_dir}/%j.stderr --output={slurm_log_dir}/%j.stdout "

command += f"{jobscript} "

eprint("submit command: " + command)

p = Popen(command.split(" "), stdout=PIPE, stderr=PIPE)
output, error = p.communicate()
if p.returncode != 0:
    raise Exception("Job can't be submitted\n"+output.decode("utf-8")+error.decode("utf-8"))
else:
    res= output.decode("utf-8")
    jobid= int(res.strip().split()[-1])

    # print jobid for snakemake
    print(jobid)
