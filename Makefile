TARGET ?= ./

lint:
	flake8 --statistics --count $(TARGET) || true

test: lint
	pytest $(TARGET)

