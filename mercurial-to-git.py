#!/usr/bin/env python2
## -*- coding: utf-8 -*-
path_to_git_export="path_to_your_git_directory" 
path_to_hg_repo="path_to_your_mercurial_project"
encoding = '1251'

# 
import os
import shutil
from subprocess import call
import platform
from os.path import relpath
fast_export_clone='git clone https://github.com/frej/fast-export.git'


temp_authors_file = 'authors.txt'
temp_branches_file = 'branches.txt'

os.chdir(path_to_hg_repo)

call('hg log | grep user: | sort | uniq | sed \'s/user: *//\' > ' + temp_authors_file, shell=True)
call('hg log | grep branch: | sort | uniq | sed \'s/user: *//\' > ' + temp_branches_file, shell=True)

# call('hg log | grep user: | sort | uniq | sed \'s/user: *//\' > ' + temp_authors_file, shell=True)
authors = []
with open('authors.txt','r') as authors_file:
	authors = authors_file.readlines()

with open('authors.txt','w') as authors_file:
	for author in authors:
		author = author.split(' ')
		length = len(author)
		author[length - 1] = author[length - 1].replace('\n', '')
		if length == 1:
			if '@' in author[0]:
				author = "\"" + author[0][:author[0].index("@")] + "\"=\"" + author[0] + "\"\n"
			else:
				author = "\"" + author[0] + "\"=\"" + author[0] + "\"\n"
		elif (length == 2):
			author = "\"" + author[0] + "\"=\"" + author[1] + "\"\n"
		else:
			author = "\"" + author[0] + "\"=\"" + ' '.join([str(x) for x in author]) + "\"\n"
		authors_file.write(author)
authors_file.close

branches = []
with open('branches.txt','r') as branch_file:
	branches = branch_file.readlines()

with open('branches.txt','w') as branch_file:
	for branch in branches:
		branch = branch.split('      ')
		if len(branch) == 2:
			branch[1] = branch[1].replace('\n', '')
			branch = "\"" + branch[0] + "\"=\"" + branch[1] + "\"\n"
			branch_file.write(branch)
branch_file.close()	


os.chdir(path_to_git_export)
call('git config core.ignoreCase false', shell=True)
temp_dir_name = "temp_dir"
call('mkdir ' + temp_dir_name, shell=True)
temp_dir = path_to_git_export + os.path.sep + temp_dir_name
temp_authors = temp_dir + os.path.sep + temp_authors_file
temp_branches = temp_dir + os.path.sep + temp_branches_file
shutil.move(path_to_hg_repo + os.path.sep + temp_authors_file, temp_dir + os.path.sep + temp_authors_file)
shutil.move(path_to_hg_repo + os.path.sep + temp_branches_file, temp_dir + os.path.sep + temp_branches_file)


os.chdir(path_to_git_export)
separator = os.path.sep
# temp_dir/fast-export/hg-fast-export.sh -r ../pgate/ -A temp_dir/authors.txt -e 1251 -B temp_dir/branches.txt -e 1251 --force
temp_path = relpath(temp_dir, path_to_git_export)
# fast_export_sh = temp_path + separator + 'fast-export' + separator + 'hg-fast-export.sh' + ' -r '
fast_export_sh = '../fast-export' + separator + 'hg-fast-export.sh' + ' -r '
authors_command = ' -A ' + temp_dir_name + separator + temp_authors_file + ' -e ' + encoding
brances_command = ' -B ' + temp_dir_name + separator + temp_branches_file + ' -e ' + encoding


r_path = relpath(path_to_hg_repo, path_to_git_export)
migrate_command = fast_export_sh + r_path + authors_command + brances_command + ' --force'

if platform.system() == 'Windows':
	convert = {'\\':'/'}
	new_migrate_command = []
	for ch in migrate_command:
		if ch == '\\':
			ch = '/'
		new_migrate_command.append(ch)
	nmc = ''.join(new_migrate_command)
else:
	nmc = migrate_command


call('echo ============= Call the following command, execute it, and then remove the ' + temp_dir_name + ' directory =============', shell=True)
call('echo ' + nmc, shell=True)
call('echo ===========================================', shell=True)










