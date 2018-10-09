if !has("python3")
    echo "vim has to be compiled with +python to run this"
    finish
else
	let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

python3 << EOF
# Standard code to include python code from a python folder
import sys
from os.path import normpath, join
import vim
plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'python'))
sys.path.insert(0, python_root_dir)
from Main import *
EOF

	command! -nargs=0 PrintInfo :python3 print_info()
	command! -nargs=0 CenterText :python3 center_text()
	command! -nargs=1 CenterTextOfLength :python3 center_text_of_length(<f-args>)

	finish
endif



















