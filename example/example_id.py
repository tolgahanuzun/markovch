from markovch import markov

diagram = markov.Markov('./data_id.txt')
diagram.check_state()

for x in range(40):
    diagram.next_state()
