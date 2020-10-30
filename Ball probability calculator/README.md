
## Ball probability calculator

Dev. by : **Radwane Ait Ouhani**.

Context : **'Scientific Computing with python'** certification project on **FreeCodeCamp**.

### The idea :

    Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 green balls. What is 
 the probability that a random draw of 4 balls will contain at least 1 red ball and 2 green
 balls? While it would be possible to calculate the probability using advanced mathematics
 an easier way is this program that perform a large number of experiments to estimate
 an approximate probability.

### The dev. :

    The Hat class have a `draw` method that accepts an argument indicating the number
 of balls to draw from the hat. This method remove balls at random from contents 
 and return those balls as a list of strings. The balls does not go back into the hat
 during the draw, similar to an urn experiment without replacement. If the number of balls
 to draw exceeds the available quantity, it returns all the balls.

Next, an experiment `function`. 
This `function`  accept the following arguments:

    * `hat`: A hat object containing balls that should be copied inside the function.
    * `expected_balls`: An object indicating the exact group of balls to attempt to draw from
        the hat for the experiment. For example, to determine the probability of drawing 2
        blue balls and 1 red ball from the hat, set expected_balls to {"blue":2, "red":1}.
    * `num_balls_drawn`: The number of balls to draw out of the hat in each experiment.
    * `num_experiments`: The number of experiments to perform. (The more experiments performed, 
        the more accurate the approximate probability will be.)

The `experiment` function returns a probability.

### Example :

For example, let's say that you want to determine the probability of getting at least 2 
red balls and 1 green ball when you draw 5 balls from a hat containing 6 black, 4 red, 
and 3 green. To do this, we perform `N` experiments, count how many times `M` we get at least 
2 red balls and 1 green ball, and estimate the probability as `M/N`. Each experiment 
consists of starting with a hat containing the specified balls, drawing a number of balls,
 and checking if we got the balls we were attempting to draw.

Here is how you would call the experiment function based on the example above with 2000
experiments:
```py
    hat = Hat(black=6, red=4, green=3)
    probability = experiment(hat=hat, 
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
    hat = Hat(black=6, red=4, green=3)
    probability = experiment(hat=hat, 
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
```

Since this is based on `random` draws, the probability will be slightly different each time the code is run.

