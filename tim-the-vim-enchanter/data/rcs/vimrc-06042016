                                                  
    "▄▄▄▄▄     ██                  ▄▄              
    "▀▀▀██     ▀▀                  ██              
       "██   ████     ████▄██▄     ▀▀     ▄▄█████▄ 
       "██     ██     ██ ██ ██            ██▄▄▄▄ ▀ 
       "██     ██     ██ ██ ██             ▀▀▀▀██▄ 
 "█▄▄▄▄▄██  ▄▄▄██▄▄▄  ██ ██ ██            █▄▄▄▄▄██ 
  "▀▀▀▀▀    ▀▀▀▀▀▀▀▀  ▀▀ ▀▀ ▀▀             ▀▀▀▀▀▀  
                                                  
                                                  
                                                            
                        "██                                  
                        "▀▀                                  
           "██▄  ▄██   ████     ████▄██▄   ██▄████   ▄█████▄ 
            "██  ██      ██     ██ ██ ██   ██▀      ██▀    ▀ 
            "▀█▄▄█▀      ██     ██ ██ ██   ██       ██       
    "██       ████    ▄▄▄██▄▄▄  ██ ██ ██   ██       ▀██▄▄▄▄█ 
    "▀▀        ▀▀     ▀▀▀▀▀▀▀▀  ▀▀ ▀▀ ▀▀   ▀▀         ▀▀▀▀▀  
                                                            
                                                            
 
" This is my personal customization of Vim
" Feel free to reference it for your own use
"
" Press <space> to open or close a section

" Window Config {{{
" Include filename in window title
autocmd BufEnter * let &titlestring = ' ' . expand("%:p")             
set title
" }}}
" Startup  {{{
set nocompatible
set ttyfast                     " faster screen redraw
set modelines=3                 " check first/last {n} lines for mode
set backspace=indent,eol,start  " enable normal backspace behavior
    " Pathogen {{{
    " load plugins and generate pathogen helptags
    call pathogen#infect()
    " }}}
    " AutoGroups {{{
    augroup configgroup
        " filetype specific settings loaded on start
        autocmd!
        autocmd VimEnter * highlight clear SignColumn
        autocmd BufWritePre *.pl,*.php,*.py,*.js,*.txt,*.hs,*.java,*.md,*.rb,*.c,*.h,*.cpp 
                    \:call <SID>StripTrailingWhitespaces()
        autocmd BufEnter *.cls setlocal filetype=java
        autocmd BufEnter Makefile setlocal noexpandtab
        autocmd BufEnter *.sh setlocal tabstop=2
        autocmd BufEnter *.sh setlocal shiftwidth=2
        autocmd BufEnter *.sh setlocal softtabstop=2
    augroup END
    " }}}
" }}}
" Colors {{{
set guifont = "Menlo:12"
colorscheme badwolf             " uses the badwolf colorscheme
set background = "dark"
    " Colorschemes {{{
        " Badwolf {{{
        let g:badwolf_darkgutter = 1
        let g:badwolf_tabline = 2
        let g:badwolf_css_props_highlight = 1
        let g:badwolf_html_link_underline = 1
        " }}}
    " }}}
" }}}
" Indentation {{{
    " Tab {{{
    set tabstop=4                   " 4 space tab
    set softtabstop=4               " 4 space tab
    set shiftwidth=4                " 4 space <</>>
    set expandtab                   " use spaces for tabs
    "   }}}
   " Autoindent {{{
    syntax on
    filetype plugin indent on
    set autoindent                  " enable autoindent
    "   }}}
" }}}
" UI Config {{{
set visualbell                  " make it stop making noise
set showmatch                   " higlight matching enclosures
set showcmd                     " show active command
set number                      " show line numbers
set ruler
set nocursorline                " don't highlight line where cursor is
set wildmenu                    " enable tab-completion
" }}}
" Searching {{{
set ignorecase                  " case insensitive search
set smartcase                   " ... unless we REALLY mean it 
                                " (makes ignorecase lower-case insensitive)
set incsearch                   " search as characters are entered
set hlsearch                    " highlight all search term matches
" }}}
" Folding {{{
set foldmethod=syntax           " fold according to language specific syntax
set foldlevelstart=0            " all folds closed on file load
set foldnestmax=10              " don't go more than 10 folds deep
" }}}                               
" Key Mappings {{{
    " Moving around {{{
    " j/k will go up/down wrapped lines
    nnoremap j gj
    nnoremap k gk
    " B/E will send the cursor to the beginning/end of line
    nnoremap B ^
    nnoremap E $
    " Disable default beginning/end of line behavior
    nnoremap $ <nop>
    nnoremap ^ <nop>
    " Selects last inserted text
    nnoremap gV `[v`]
    " space will open/close folds
    noremap <space> za

    onoremap an :<c-u>call <SID>NextTextObject('a', 'f')<cr>
    xnoremap an :<c-u>call <SID>NextTextObject('a', 'f')<cr>
    onoremap in :<c-u>call <SID>NextTextObject('i', 'f')<cr>
    xnoremap in :<c-u>call <SID>NextTextObject('i', 'f')<cr>
    onoremap al :<c-u>call <SID>NextTextObject('a', 'F')<cr>
    xnoremap al :<c-u>call <SID>NextTextObject('a', 'F')<cr>
    onoremap il :<c-u>call <SID>NextTextObject('i', 'F')<cr>
    xnoremap il :<c-u>call <SID>NextTextObject('i', 'F')<cr>
        " }}}
    " Map Leader tied {{{
    let mapleader="\\"
    " force redraw of screen
    nnoremap <leader>m :silent make\|redraw!\|cw<CR>
    " Check for errors
    nnoremap <leader>c :SyntasticCheck<CR>:Errors<CR>
    " Start NERDTree
    nnoremap <leader>w :NERDTree<CR>
    " Start Gundo
    nnoremap <leader>u :GundoToggle<CR>
    " Start silver searcher
    nnoremap <leader>a :Ag 
    nnoremap <leader>h :A<CR>
    " Toggle number scroll
    nnoremap <leader>l :call ScrollNumber()<CR>
    " Toggle line numbers
    nnoremap <leader>1 :set number!<CR>
    " Clear highlighting
    nnoremap <leader><space> :noh<CR>
    " Save session settings
    nnoremap <leader>s :mksession<CR>
    " going into visual mode on folded code will expand it
    vmap v <Plug>(expand_region_expand)
    vmap <C-v> <Plug>(expand_region_shrink)
    vnoremap <C-c> "*y
    " }}}
" }}}
" Plugin Configs {{{
    " Airline {{{
    let g:airline#extensions#tabline#left_sep = ' '
    let g:airline#extensions#tabline#left_alt_sep = '|'
    let g:airline_left_sep = ''
    let g:airline_left_alt_sep = ''
    let g:airline_right_sep = ''
    let g:airline_right_alt_sep = ''
    set laststatus=2
        " }}}
    " CtrlP {{{
    let g:ctrlp_match_window = 'bottom,order:ttb'
    let g:ctrlp_switch_buffer = 0
    let g:ctrlp_working_path_mode = 0
    let g:ctrlp_custom_ignore = '\vbuild/|dist/|venv/|target/|\.(o|swp|pyc|egg)$'
    " }}}
    " Gundo {{{
    if has("python3") && !has("python")
        let g:gundo_prefer_python3 = 1
    endif
    " }}}
    " NERDTree {{{
    let NERDTreeIgnore = ['\.pyc$', 'build', 'venv', 'egg', 'egg-info/', 'dist', 'docs']
    " }}}
    " Syntastic {{{
    let g:syntastic_python_flake8_args='--ignore=E501'
    let g:syntastic_ignore_files = ['.java$']
    " }}}
    " Tabular {{{
    nnoremap <leader>a= :Tabularize /=<CR>
    vnoremap <leader>a= :Tabularize /=<CR>
    nnoremap <leader>a: :Tabularize /:\zs<CR>
    vnoremap <leader>a: :Tabularize /:\zs<CR>
    " }}}
   
" }}} 
" Custom Functions {{{ 
function! <SID>SaveUIStateAndProcess(cmd)
    let _s=@/ 
    let l=line(".")
    let c=col(".")
    execute a:cmd
    let @/=_s
    call cursor(l,c)
endfunction

" ::RmTrailingWhitespace
function! <SID>RmTrailingWhitespace()
    call SaveUIStateAndProcess("normal gg=G")
    " %s/\s\+$//e
endfunction


function! <SID>CleanFile()
	call SaveUIStateAndProcess("%!git stripspace")
endfunction

" ::ScrollNumber
" Toggles whether we want to scroll line numbers with cursor with a range above and below
function! ScrollNumber()
    if(&relativenumber == 1)
        set norelativenumber
        set number
    else
        set relativenumber
    endif
endfunction

function! s:NextTextObject(motion,dir)
	let c=nr2char(getchar())
	if c==#"b"
        let c="("
	elseif c==#"B"
        let c="{"
	elseif c==#"r" 
        let c="["
	endif
	exe "normal! ".a:dir.c."v".a:motion.c
endfunction
"}}}
" Modeline {{{
" vim: foldmethod=marker:foldlevel=0
" }}}
