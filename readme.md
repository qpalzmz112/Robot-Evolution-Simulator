# Assignment 8: Evolve Morphology and Behavior for Locomotion
To run, clone and run `trial.py`. This will run five trials, each with population size and number of generations specified in constants.py. Then, it will generate a graph showing the maximum fitness per generation in each trial. If you want to see the best robot of each trial, uncomment the following code:  
    `#input("Press Enter to continue...")`<br>
    `#phc.Show_Best()`<br>
    `#input("Press Enter to continue...")`<br>
Then, when a trial is done, you will be prompted to press enter to view the best robot. Once this is done you may not see a prompt, but press enter to begin the next trial.

## How are bodies and brains generated?
Take a look at [this](https://github.com/qpalzmz112/ludobots/tree/Assignment7#readme) readme.

## How are bodies evolved?
Mutations are randomly selected from two options: adding a link or changing a synapse weight. In the former case, a random 'leaf' link is selected, and a random link is added to it as described in the body generation section [here](https://github.com/qpalzmz112/ludobots/tree/Assignment7#readme). By leaf link, I mean a link that is the child of a joint but is not the parent of any joints. Basically, the leaf links are the links that are furthest from the root of the robot.<br>
<img src="https://user-images.githubusercontent.com/68213464/221488995-4e9f2ef5-7682-4e6a-a511-9a9e67887cb9.png" width="500" height="500">
## How are brains evolved?
When a synapse weight is changed, a random synapse is chosen and its weight is updated to a random number, still subject to the motorJointRange constraint defined in constants.py.

## Sources:
CS 396: Artifial Life at Northwestern University, r/ludobots, and [pyrosim](https://github.com/jbongard/pyrosim).
