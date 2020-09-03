# s2s-profiles
Easy [snakemake profile](https://snakemake.readthedocs.io/en/stable/executable.html#profiles) installation for either local computers or slurm clusters. 

## Installation
Installation has been made extremely easy and is done by [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)! 

Start with cloning the repo locally and moving into the directory:

    git clone git@github.com:vanheeringen-lab/seq2science-profiles.git
    cd seq2science-profiles
    
### local machine installation
`cookiecutter -f local`

or with one of the provided configfiles (mb07 or threadripper):

`cookiecutter -f --config-file=local/[[configfile]] local`

### slurm installation
`cookiecutter -f slurm`

or with one of the provided configfiles (moldev):

`cookiecutter -f --config-file=slurm/[[configfile]] slurm`

### input
During the installation process users are prompted for input, these are the inputs we feel might need explanation:
- **resources**, **config**, **additional**, **default_rule**: comma separated string of key-value pairs; e.g. "key1: val1, key2: val2"
- **optional_rules**: comma separated string of rule(key-value) pairs; e.g. "rule1(key1: val1, key2: val2), rule2(key3: val3)"

If added, the keys must be recognized by the [snakemake API](https://snakemake.readthedocs.io/en/stable/api_reference/snakemake.html)

These inputs only allow dictionaries (lists or nested dicts can be added afterward).

### output
A profile that can be passer to `seq2science` using `seq2science ... --profile profile_name`.

The file can be found in `~/.config/snakemake/profile_name/config.yaml`.
