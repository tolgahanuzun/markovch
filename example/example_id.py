from markovch import markov

diagram = markov.Markov('./data_id.txt')

print(diagram.result_list(50))
