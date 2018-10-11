" Set the plugin absolute path to a variable
let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

function! LoadVimCenter()
	if has("python3")
		command! -nargs=0 PrintInfo :python3 print_info()
		command! -nargs=0 CenterText :python3 center_text()
		command! -nargs=1 CenterTextOfLength :python3 center_text_of_length(<f-args>)
	elseif has("python")
		command! -nargs=0 PrintInfo :python print_info()
		command! -nargs=0 CenterText :python center_text()
		command! -nargs=1 CenterTextOfLength :python center_text_of_length(<f-args>)
	endif
endfunction

" Include the python folder so that we can call python functions defined within that folder
exec "source " . s:plugin_root_dir . "/include-python-folder.vim"

" Load/define the vim commands that will call our python functions
call LoadVimCenter()




