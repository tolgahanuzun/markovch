# Markov Chain

- It's a simple Markov chain implementation. It gets the data from a txt file. Future value analysis and proportions.

## How to install?
Install with Pip.

```
pip install markovch
```

## Simple code

```python
from markovch import markov

diagram = markov.Markov('./data_eng.txt')
diagram.check_state() # Head value print

for x in range(40): #Total predictions.
    diagram.next_state()
```

### Todo

* It must be run with json data.
* The functions can be updated.
