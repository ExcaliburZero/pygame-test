PACKAGE = pygametest

help:
	@echo "The following make commands are valid, and can be run as 'make COMMAND':"
	@echo ""
	@echo "  run	runs the game"
	@echo "  test   tests the game"
	@echo ""

run:
	python $(PACKAGE)/window.py

test:
	nosetests
