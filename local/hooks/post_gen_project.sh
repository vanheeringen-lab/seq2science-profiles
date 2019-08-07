#!/bin/sh

# if no snakemake configuration
if [ ! -d "$HOME/.config/snakemake/" ]; then
  mkdir "$HOME/.config/snakemake/"
fi

# if the profile already exists delete it
if [ -d "$HOME/.config/snakemake/{{cookiecutter.profile_name}}" ]; then
  rm -r "$HOME/.config/snakemake/{{cookiecutter.profile_name}}/"
fi

# make a directory for the profile
mkdir "$HOME/.config/snakemake/{{cookiecutter.profile_name}}"

# now place it in the snakemake profiles
cd ..
mv {{cookiecutter.profile_name}} "$HOME/.config/snakemake/{{cookiecutter.profile_name}}"
