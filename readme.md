# Final project: Does the number of links in a robot's body correlate with its ability to move?
To run, clone and run `trial.py`. This will run five trials, each with population size and number of generations specified in constants.py. Then, it will generate a graph showing the maximum fitness per generation in each trial. If you want to see the best robot of each trial, uncomment the following code:  
    `#input("Press Enter to continue...")`<br>
    `#phc.Show_Best()`<br>
    `#input("Press Enter to continue...")`<br>
Then, when a trial is done, you will be prompted to press enter to view the best robot. Once this is done you may not see a prompt, but press enter to begin the next trial. To change the maximum number of links a robot can have, edit `maxLinks` in `constants.py`.

## Hypothesis:
Robots with more links will move further than robots with few links. The reasoning for this hypothesis comes from the fact that my simulator is very simple. Each joint rotates about one axis, and I expect robots which have links rotating about more axes to move further than robots with links rotating about fewer axes.

This experiment is motivated by an observation made by Professor Kriegman: some of Karl Sims' [robots](https://www.karlsims.com/evolved-virtual-creatures.html) move very well with only a few links constituting their bodies. I'd like to see if my simulator can achieve similar results, or if its simplicity requires robots to have more links than Sims'.

From this I hope to contribute to the answers to two questions: "How many parts should make up the body of a robot evolved for locomotion?" and "How do the differences in variety and complexity of random robot bodies affect the robots' ability to move?" In any case, my results will give some insight into the first question. If my hypothesis is correct, it would appear that Sims' more advanced range of robot bodies is capable of generating better robots than my simulator, which would be relevant to the second question.

## How are bodies and brains generated?
Take a look at [this](https://github.com/qpalzmz112/ludobots/tree/Assignment7#readme) readme.

## How are robots evolved?
Take a look at [this](https://github.com/qpalzmz112/ludobots/tree/Assignment8#readme) readme.

## Sources:
CS 396: Artificial Life at Northwestern University, r/ludobots, and [pyrosim](https://github.com/jbongard/pyrosim).
