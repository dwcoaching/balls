from simulator import Simulator
import sys

number_of_tries = int(sys.argv[1])
simulator = Simulator(number_of_tries)
stats = simulator.getStats()
probabilty = stats['white_balls_on_the_first_step']['white_balls_on_the_second_step_count'] / stats['white_balls_on_the_first_step']['count']

print('TOTAL NUMBER OF TRIES: ' + str(number_of_tries) + '\n')
print('WHITE BALLS ON THE FIRST STEP: ' + str(stats['white_balls_on_the_first_step']['count']))
print('   Second step, white balls: ' + str(stats['white_balls_on_the_first_step']['white_balls_on_the_second_step_count']))
print('   Second step, black balls: ' + str(stats['white_balls_on_the_first_step']['black_balls_on_the_second_step_count']))
print()
print('BLACK BALLS ON THE FIRST STEP: ' + str(stats['black_balls_on_the_first_step']['count']))
print('   Second step, white balls: ' + str(stats['black_balls_on_the_first_step']['white_balls_on_the_second_step_count']))
print('   Second step, black balls: ' + str(stats['black_balls_on_the_first_step']['black_balls_on_the_second_step_count']))
print()
print('PROBABILITY: ' + str(probabilty))

