from markovch import markov

diagram = markov.Markov('./data_eng.txt')

print(diagram.result_list(50))
