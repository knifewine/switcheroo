#!/usr/bin/env python
import argparse
import os
import subprocess
from dumbcolor import colorize


parser = argparse.ArgumentParser()
parser.add_argument("--symlink-file", help="symlink file path. this is a symlink whose target can/will be updated.")
parser.add_argument("--options", help="list of paths to choose from. when a choice is made it will become the symlink target")
parser.add_argument("--chosen-env-var", help="(optional) env var already pointing to the symlink file path. when specified the env var will checked to make sure it points to the symlink provided.")
parser.add_argument("--show-git-branch", help="(optional) enable showing git branch on paths. this will blow up if the paths aren't currently versioned with git", action="store_true")

args = parser.parse_args()

if not (args.symlink_file and args.options):
    parser.print_help()
    exit(0)

symlink_path = os.path.abspath(args.symlink_file)

# the whole point of providing a chosen_env_var is just so we can check that it points to the symlink as a convenience
# so this is optional, and not required if you just need to switch a symlink between targets
# -- but assuming you are using some system that looks in $ENV_VAR (which contains a symlink path) it will warn you if unset or set wrong
if args.chosen_env_var:
    current_choice = os.environ.get(args.chosen_env_var, None)
    if not current_choice == symlink_path:
        print "please set {} to {}".format(args.chosen_env_var, symlink_path)
        print "  e.g. export {}={}".format(args.chosen_env_var, symlink_path)
        exit(1)

possible_dirs = [d for d in args.options.split(':') if len(d) > 0]

if os.path.exists(symlink_path) and os.path.islink(symlink_path):
    if args.chosen_env_var:
        print "{env_var} is {currently} linked to {target}\n".format(
            env_var=colorize(args.chosen_env_var, 'blue'),
            currently=colorize('currently', 'red'),
            target=colorize(os.readlink(symlink_path), 'green')
        )
    else:
        print "symlink at {symlink_path} is {currently} linked to {target}\n".format(
            symlink_path=colorize(symlink_path, 'blue bold'),
            currently=colorize('currently', 'red'),
            target=colorize(os.readlink(symlink_path), 'green bold underline')
        )

for idx, dirname in enumerate(possible_dirs, 1):
    if args.show_git_branch is True:
        git_label = subprocess.check_output(["git", "status"], cwd=dirname).split("\n")[0]
        print "{idx}. {dirname} ({git_label})".format(idx=idx, dirname=dirname, git_label=git_label)
    else:
        print "{idx}. {dirname}".format(idx=idx, dirname=dirname)

choice = raw_input("\nplease choose a number (enter to quit): ")

try:
    int_choice = int(choice)
except ValueError:
    if len(choice) == 0:
        print "quitting"
        exit(0)

    print "invalid choice"
    exit(1)

if (int_choice <= 0) or int_choice > len(possible_dirs):
    print "invalid number"
    exit(1)


if os.path.exists(symlink_path):
    # unlink symlink's current target
    if os.path.islink(symlink_path):
        os.unlink(symlink_path)

    os.symlink(possible_dirs[int_choice - 1], symlink_path)
    if args.chosen_env_var:
        print "{envvar} is {now} linked to {symlink_target}\n".format(
            envvar=colorize(args.chosen_env_var, 'blue bold'),
            now=colorize('now', 'red bold underline'),
            symlink_target=colorize(os.readlink(symlink_path), 'green bold underline')
        )
    else:
        print "symlink at {symlink_loc} is {now} linked to {symlink_target}\n".format(
            symlink_loc=colorize(symlink_path),
            now=colorize('now', 'red'),
            symlink_target=colorize(os.readlink(symlink_path), 'green bold underline')
        )
