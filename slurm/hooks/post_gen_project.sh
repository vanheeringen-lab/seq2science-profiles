#!/bin/sh

# if the profile already exists delete it
rm -rf "$HOME/.config/snakemake/{{cookiecutter.profile_name}}/"

# make a directory for the profile
mkdir -p "$HOME/.config/snakemake/{{cookiecutter.profile_name}}"

# now place the output in the snakemake profiles directory
cd ..
mv {{cookiecutter.profile_name}} "$HOME/.config/snakemake/"

# and replace the ~ with /home/user
sed -i "s|\~|${HOME}|" ~/.config/snakemake/{{cookiecutter.profile_name}}/config.yaml

# finally make the scheduler script executable
chmod +x ~/.config/snakemake/{{cookiecutter.profile_name}}/scheduler.py
