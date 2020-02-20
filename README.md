# Mercurial to git migration script

## Descripton

This script allows to migrate the project from mercurial to git. It uses the [fast export](https://github.com/frej/fast-export.git). 

## What it needs

* python2.7
* `pip install mercurial` 

## How it works

Change in script two fields: `path_to_git_export` and `path_to_hg_repo` and run it. The script will give you a command you should run in console. After doing remove from result git project a `temp_dir` folder.

## What problem you may have

* On Windows it may be needed to run scrupt in git-console
* Depends on your OS it may be different path separator
* Link (or version) to [fast export](https://github.com/frej/fast-export.git) may be invalid (can be fixed by founding of right version or download another version)
* Closed branches will be active in git project
