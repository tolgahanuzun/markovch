import numpy as np
from functools import reduce


class Markov(object):

    def __init__(self, state_dict, text=True):
        self.data = self.read_file(state_dict)
        self.uniqe_data = self.uniqe_list(self.data)
        self.markov = self.markov_data(self.uniqe_data, self.data)
        self.state_dict = self.analytic(self.markov)
        self.state = self.data[0][0]
        self.result_data = None

    def check_state(self):
        return self.state

    def set_state(self, state):
        self.state = state
        return self.state

    def next_state(self):
        A = self.state_dict[self.state]
        self.state = np.random.choice(a=list(A[0]), p=list(A[1]))
        return self.state

    def read_file(self, file_name):
        with open(file_name, 'r') as f:
            rows = [line.strip('\n') for line in f]
        return [row.split() for row in rows]

    def uniqe_list(self, data_list):
        return reduce(lambda a, b: set(a) | set(b), data_list)

    def convert_dict(self, uniqe_list):
        new_dict = {}
        for uniqe in uniqe_list:
            new_dict[uniqe] = list()
        return new_dict

    def markov_data(self, uniqe_list, data_list):
        new_dict = self.convert_dict(uniqe_list)

        for uniqe in new_dict:
            for data in data_list:
                if uniqe in data:
                    next_element = data.index(uniqe)+1
                    if len(data) != next_element:
                        new_dict[uniqe] = new_dict[uniqe] +  [data[next_element]]
                    else:
                        new_dict[uniqe] = new_dict[uniqe] + [self.data[0][0]]
            new_dict[uniqe] = set(new_dict[uniqe])    
        return new_dict

    def analytic(self, markov):
        for datas in markov:
            if len(markov[datas]):
                markov[datas] = markov[datas], np.full(len(markov[datas]), 1/len(markov[datas]))
        return markov

    def loop_state(self, loop):
        return [self.next_state() for row in range(loop)]

    def sentence_true(self, loop):
        self.result_data = [self.state] + self.loop_state(loop)
        a = ['?' in data for data in self.result_data]
        b = ['.' in data for data in self.result_data]
        c = ['!' in data for data in self.result_data]
        d = [':' in data for data in self.result_data]

        return list(map(lambda x, y, z, k: x + y + z + k, a, b, c, d))

    def diffirent_sentence(self, data, data_true):
        if not sum(data_true):
            return []
        else:
            index = data_true.index(1) + 1
            return [data[:index]] + self.diffirent_sentence(data[index:],data_true[index:])

    def result_list(self, loop):
        data_true = self.sentence_true(loop)
        if 1 in data_true:
            return self.diffirent_sentence(self.result_data, data_true)
        else:
            return self.result_data
