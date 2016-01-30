PACKAGE = pygametest

help:
	@echo "The following make commands are valid, and can be run as 'make COMMAND':"
	@echo ""
	@echo "  run            runs the game"
	@echo "  test           runs tests of the game"
	@echo "  testcoverage   runs tests of the game with coverage"
	@echo ""

run:
	python $(PACKAGE)/window.py

test:
	nosetests --cover-package=$(PACKAGE)

testcoverage:
	nosetests --with-coverage --cover-package=$(PACKAGE)
