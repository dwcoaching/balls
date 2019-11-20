class Basket

    def initialize
        @balls = []
        @balls << WHITE

        second_rand = rand(1..5)

        if second_rand == 1
            @balls << BLACK
        else
            @balls << WHITE
        end

        third_rand = rand(1..5)

        if third_rand == 1
            @balls << WHITE
        elsif third_rand <= 3
            @balls << BLACK
        else
            @balls << RED
        end
    end

    def take_ball
        random = rand(0..(@balls.length - 1))
        ball = @balls[random]
        @balls.delete_at(random)

        return ball
    end

    def get_balls
        return @balls
    end

end
