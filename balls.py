from simulator import Simulator

simulator = Simulator(10000)
stats = simulator.getStats()

print(stats)
print('\nProbabilty:')
print(stats['white_balls_on_the_first_step']['white_balls_on_the_second_step_count']
    / stats['white_balls_on_the_first_step']['count'])

