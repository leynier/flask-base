host = 0.0.0.0
port = 5000

run:
	@export FLASK_APP=run.py &&\
	export FLASK_ENV=development &&\
	export FLASK_DEBUG=1 &&\
	flask run --host=${host} --port=${port}

run_pro:
	@export FLASK_APP=run.py &&\
	export FLASK_ENV=production &&\
	export FLASK_DEBUG=0
	flask run --host=${host} --port=${port}

shell:
	@export FLASK_APP=run.py &&\
	flask shell
