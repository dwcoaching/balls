from basket import Basket

class Simulator:
    def __init__(self, number):
        self.baskets = []
        self.stats = {'white_balls_on_the_first_step': {
            'count': 0,
            'white_balls_on_the_second_step_count': 0,
            'black_balls_on_the_second_step_count': 0
            },
            'black_balls_on_the_first_step': {
            'count': 0,
            'white_balls_on_the_second_step_count': 0,
            'black_balls_on_the_second_step_count': 0
            }
        }

        for i in range(0, number):
            self.baskets.append(Basket())

        self.run()

    def run(self):
        for basket in self.baskets:
            first_ball_color = basket.getBall()
            second_ball_color = basket.getBall()

            if first_ball_color == 'white':
                self.stats['white_balls_on_the_first_step']['count'] +=1
                if (second_ball_color == 'white'):
                    self.stats['white_balls_on_the_first_step']['white_balls_on_the_second_step_count'] +=1
                elif (second_ball_color == 'black'):
                    self.stats['white_balls_on_the_first_step']['black_balls_on_the_second_step_count'] +=1
            elif first_ball_color == 'black':
                self.stats['black_balls_on_the_first_step']['count'] +=1
                if (second_ball_color == 'white'):
                    self.stats['black_balls_on_the_first_step']['white_balls_on_the_second_step_count'] +=1
                elif (second_ball_color == 'black'):
                    self.stats['black_balls_on_the_first_step']['black_balls_on_the_second_step_count'] +=1

    def getStats(self):
        return self.stats
