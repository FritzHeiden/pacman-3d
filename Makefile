install_virtenv:
	env PYTHON_CONFIGURE_OPTS="--enable-framework CC=clang" pyenv install 3.5.3

init_virtenv:
	#env PYTHON_CONFIGURE_OPTS="--enable-framework CC=clang" pyenv install 3.5.3 
	pyenv virtualenv 3.5.3 pacman
	pyenv local pacman

first_init:
	make install_virtenv
	make init_virtenv
	make init

init:
	pip install --upgrade pip
	pip install pip-tools
	pip-compile
	pip-sync

run:
	python pacman-3d/core.py

build:
	pyinstaller --windowed pacman-3d/core.py

clean:
	rm -rf dist/* build/*

cleanall:
	rm -rf dist/ build/
	pyenv uninstall pacman
	rm -f python-version

mrpropper:
	make cleanall
	pyenv uninstall 3.5.3

help:
	@echo  'Init Project:'
	@echo  '  first_init      - Run install_virtenv, init_virtenv and init'
	@echo  '  install_virtenv - Install pyenv 3.5.3'
	@echo  '  init_virtenv    - Setup virtual environment "pacman", set it as local'
	@echo  '  init            - Upgrade pip to latest, install pip-tools, fetch'
	@echo  '                    and install required packages from requirements.in'
	@echo  ''
	@echo  'Run Project:'
	@echo  '  run 			  - Run pacman-3d/core.py
	@echo  'Build Project:'
	@echo  '  build		  - Build executable file in dist folder'
	@echo  ''
	@echo  'Cleaning Project:'
	@echo  '  clean           - Clean dist and build folder'
	@echo  '  cleanall        - Remove dist and build folder, delete pacman virtenv'
	@echo  '                    and remove local python version'
	@echo  '  mrpropper	  - Run cleanall and uninstall used pyenvv (3.5.3)'
	@echo  ''