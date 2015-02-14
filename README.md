# switcheroo
...Is a simple python program for switching a symlink target between choices.
It's nice for working with software that looks in a single place for things (config files, git repositories, etc.) so you can point it to a new location without too much work.

# Huh?
Lots of software likes to look in specific locations for files or directories.
But you're clever so you tell that software about a symlink instead.
And then you use this simple tool to change where the symlink points on demand.
Then instead of copying files around or munging environment variables, your location is found through the symlink.
Now you can keep multiple configs, directories, etc. for the program to use, and readily switch between them without it caring.

If the software you are using with switcheroo makes you tell it about the file/location with an environment variable like CONFIG_FILE, you can tell switcheroo about this environment variable and it will nag you to set the environment variable to the symlink location.

If the symlink choices are directories versioned with git, you can have switcheroo include the branch information as well.

## Use as part of an alias for more flexibility
Switcheroo is meant to be aliased in your shell so you don't have to remember all the options.

Something like this in your .bashrc will get your a switcher with git branch awareness:

    export CURRENT_LOCATION=/home/russ/important_location  # this is (or will become) a symbolic link
    export LOCATION_CHOICES=/home/russ/important_ONE:/home/russ/important_TWO:/home/russ/some_other_wacky_place  # colon-delimited paths
    alias switcher='switcheroo.py --symlink-file $CURRENT_LOCATION --options $LOCATION_CHOICES --chosen-env-var CURRENT_LOCATION --show-git-branch'

  
