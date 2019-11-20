class Simulator

    def initialize_results
        @results = {}

        balls = [WHITE, BLACK, RED]

        balls.each do |first|
            @results[first] = {:count => 0}

            balls.each do |second|
                @results[first][second] = {:count => 0}

                balls.each do |third|
                    @results[first][second][third] = {:count => 0}
                end
            end
        end
    end

    def initialize(number_of_tries)
        @number_of_tries = number_of_tries
        @baskets = []

        for i in 1..number_of_tries
            @baskets << Basket.new()
        end

        self.initialize_results
    end

    def get_baskets
        return @baskets
    end

    def run
        @baskets.each do |basket|
            first_ball = basket.take_ball
            second_ball = basket.take_ball
            third_ball = basket.take_ball

            @results[first_ball][:count] += 1
            @results[first_ball][second_ball][:count] += 1
            @results[first_ball][second_ball][third_ball][:count] += 1
        end
    end

    def get_results
        return @results
    end
end
