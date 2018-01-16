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
print(diagram.result_list(50))
```

### Todo

* It must be run with json data.
* The functions can be updated.
