let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')
"
" Vim wont let you indent this code, so I put it down here to live in exile,
" outside of the plugin function.
if has("python3")
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
elseif has("python")
python << EOF
# Standard code to include python code from a python folder
import sys
from os.path import normpath, join
import vim
plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'python'))
sys.path.insert(0, python_root_dir)
from Main import *
EOF
else
	echo "vim has to be compiled with +python to run this plugin"
	finish
endif
