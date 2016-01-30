# pygame-test
This is a small test of pygame.

# Usage
To play the game, run the following command in the main directory of the project:

```
make run
```

# Development
The following is information on the development of the game.

## Testing
The game has a suit of unit tests for it, which can be run in order to test certain functionality of the game. The tests can be run by running the following command in the main directory of the project:

```
make test
```

The coverage of the unit tests can also be determined by running the following command:

```
make testcoverage
```

Travis CI is used to automatically test any branches of the repository pushed to GitHub. After every run of the test suits, the coverage of the tests is recorded by Coveralls.

# License
* **Code:** [MIT License](http://opensource.org/licenses/MIT)
* **Images:** [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
