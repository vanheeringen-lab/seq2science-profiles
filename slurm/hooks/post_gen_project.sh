#!/bin/sh

# if the profile already exists delete it
rm -rf "$HOME/.config/snakemake/{{cookiecutter.profile_name}}/"

# make a directory for the profile
mkdir -p "$HOME/.config/snakemake/{{cookiecutter.profile_name}}"

# now place the output in the snakemake profiles directory
cd ..
mv {{cookiecutter.profile_name}} "$HOME/.config/snakemake/"
