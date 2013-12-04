install:
	virtualenv venv
	venv/bin/pip install -e .

make_ln:
	ln -s `pwd`/venv/bin/pass ~/bin/
