# Assignment 7: Generate Random 3D Creature Morphologies
To run, clone and run `search.py`. This will generate a single random 'creature'

## How are bodies generated?
Each body begins with a few random constraints: a maximum dimension value for its links and a maximum 'depth'. The depth refers to
the genotype of each body, which is a direct representation structured as a tree. The root of the tree is the root link of the robot. 
Each child node of the tree is a joint connected to it, and each joint node contains one link as its own child. The depth limits how 
deep the tree will be.

After choosing these constraints, the program begins to generate the body. It starts with the root, choosing 
a random number of links to attach to the root. Then, for each of these links, it chooses a random number of links
to attach to them, and so on until the depth constraint is reached.

For each of the links added, it has randomly chosen dimensions subject to the constraint mentioned above, and a 
50% chance to contain a sensor, in which case the link is colored green. When attaching a new link to a present link,
the program chooses randomly among 9 directions. For each direction, the corresponding joint location is represented with a red dot.
An example of a possible new link is drawn in blue for two of the directions.

DIAGRAM

Each joint can move on one axis, randomly chosen among the x, y, and z-axes.

## How are brains generated?
Each green link has a sensor neuron and each joint has a motor neuron. Each sensor neuron 
is connected to each motor neuron.

## What morphologies are possible? 
The program could generate a snake or a quadruped, although this is unlikely. In most cases, the body generated
will just be a group of randomly connected rectangular prisms that bear little resemblance to anything living.

DIAGRAM

## Sources:
CS 396: Artifial Life at Northwestern University, r/ludobots, and [pyrosim](https://github.com/jbongard/pyrosim).
