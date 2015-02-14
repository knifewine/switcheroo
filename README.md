# Switcheroo
...Is a simple python program for switching a symlink target between choices.
It's nice for working with software that looks in a single place for things (config files, git repositories, etc.) so you can point it to a new location without too much work.

## Huh?
Lots of software likes to look in specific locations for files or directories.
But you're clever so you tell that software about a symlink instead.
And then you use this simple tool to change where the symlink points on demand.
Then instead of copying files around or munging environment variables, your location is found through the symlink.
Now you can keep multiple configs, directories, etc. for the program to use, and readily switch between them without it caring.

If the software you are using with switcheroo makes you tell it about the file/location with an environment variable like CONFIG_FILE, you can tell switcheroo about this environment variable and it will nag you to set the environment variable to the symlink location.

If the symlink choices are directories versioned with git, you can have switcheroo include the branch information as well.

## Install

All you need is a recent python, a color terminal, and a unix-like system. Then just clone this repo and run the script! See below for an example with arguments, and how an alias makes it more user friendly.

## Use as part of an alias for more flexibility
Switcheroo is meant to be aliased in your shell so you don't have to remember all the options.

Something like this in your .bashrc will get your a switcher with git branch awareness:

    export CURRENT_LOCATION=/home/russ/symlinks/important_location  # this is (or will become) a symbolic link
    export LOCATION_CHOICES=/home/russ/important_ONE:/home/russ/important_TWO:/home/russ/some_other_wacky_place  # colon-delimited paths
    alias switcher='/home/russ/bin/switcheroo/switcheroo.py \
      --symlink-file $CURRENT_LOCATION\
      --options $LOCATION_CHOICES\
      --chosen-env-var CURRENT_LOCATION\
      --show-git-branch'


![switcheroo in action](https://cloud.githubusercontent.com/assets/123593/6198472/ecfc5ef8-b3c0-11e4-9578-bd1cd93c8681.png)
