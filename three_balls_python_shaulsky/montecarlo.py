import numpy as np
from collections import OrderedDict

bags = [{'white':1}, {'white': .7, 'black': .3}, {'white': .2, 'black': .1, 'red': .7}]

def choose_ball(bag):
    '''
    chose ball from bag given probability
    '''
    order_bag = OrderedDict(sorted(bag.items(), key=lambda x: x[1]))
    rnd = np.random.rand(1)[0]
    cum_prob = 0
    for bc, prob in order_bag.items():
        cum_prob = cum_prob + prob
        if rnd < cum_prob:
            return bc
def select_bags(num_bags):
    '''
    return indeces orderd in random
    '''
    bags_indeces = list(range(num_bags))
    selected = []
    while bags_indeces:
        rnd = np.random.randint(0, len(bags_indeces))
        selected.append(bags_indeces.pop(rnd))
    return selected

def event(bags):
    '''
    selecct bag, and pickup ball
    '''
    indx = select_bags(len(bags))
    chosen_balls = []
    for i in indx:
        chosen_balls.append(choose_ball(bags[i]))
    return chosen_balls

def experiment(bags, iter_num=10):
    count_1 = 0
    count_2 = 0
    for _ in range(iter_num):
        balls = event(bags)
        #conditions here
        if balls[0] == 'white' and balls[1] == 'white':
            count_1 += 1
            if balls[2] == 'red':
                count_2 += 1
    return {'(P(red|white,white), events)': (count_2/count_1, count_2),
            '(P(white,white,red), events)': (count_2/iter_num, count_2),
            '(P(white,white), events)': (count_1/iter_num, count_1)}

print(experiment(bags, iter_num=int(1e6)))
