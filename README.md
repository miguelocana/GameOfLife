![Image description](logo.png)

The game of life is the best-known two-dimensional cellular automaton, invented by John H. Conway and popularized in Martin Gardner's *Scientific American* column starting in October 1970. The game of life was originally played (i.e., successive generations were produced) by hand with counters, but implementation on a computer greatly increased the ease of exploring patterns.

The life cellular automaton is run by placing a number of filled cells on a two-dimensional grid. Each generation then switches cells on or off depending on the state of the cells that surround it. The rules are defined as follows:

1. Any live cell with two or three live neighbors survives.
2. Any dead cell with three live neighbors becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.

With this script, you can just create your own parameters and play with it.

## Packages
*To install the following packages, use the pip command in your terminal.*

#### PyGame
Pygame is a set of Python modules designed for writing video games. Pygame adds functionality on top of the SDL library. This allows you to create fully featured games and multimedia programs like the Conway's Game of Life.

```python
$ pip install pygame
```
#### NumPy
NumPy is the fundamental package for scientific computing with Python. It's mostly used for working in arrays, linear algebra, fourier transform, and matrices. 

```python
$ pip install numpy
```

## How to play:
You have to run the *main.py* through your terminal like the following code:
```python
$ python main.py
```

## Controls

**PAUSE / PLAY** -> any key

**FILL CELL** -> click mouse

*Observations:* If you pause the game, you can fill any cell you want

## Patterns

