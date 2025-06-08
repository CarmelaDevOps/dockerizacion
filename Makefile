run:
	docker build -t calculadora .
	docker run -it --rm -v "$(PWD)/logs:/app/logs" calculadora

test:
	docker build -t calculadora .
	docker run --rm calculadora pytest test_calculadora.py
