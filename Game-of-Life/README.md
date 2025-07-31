# Game-of-Life
This repo contains various of my implementations of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) ("GOL") cellular automaton.

## tkinter implementation (python)
A neat implementation that runs GOL in a customisable tkinter window. The original idea was to be able to study certain sequences of patterns, and so it also features optional "pruning" or "trimming"; removing certain patterns that are deemed uninteresting and that may interfere with the interestings patterns. Those patterns are at the moment the [Block](https://conwaylife.com/wiki/Block), [Beehive](https://conwaylife.com/wiki/Beehive) and [Boat](https://conwaylife.com/wiki/Boat). Trimming is implemented in `Field_operator.py`.

- Want to try it? Run `Game_of_life_main.py` in a console. The program will ask the user to choose setup configuration. Enter "standard". The "Manual" option is supposed to let the user specify canvas size, number of squares etc, but it currently suffers from a bug where the program won't accept any format of canvas size specification.

## Command Line Interface (CLI) implementation (python)
A very simple implementation that runs GOL in the command line interface, making it very easy to use.

## TI BASIC implementation
Currently this is just a cool idea I have not yet implemented.
