from markovch import markov

diagram = markov.Markov('./data_tr.txt')

print(diagram.result_list(50))
