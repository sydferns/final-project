# Title: Block Tower Stack game

## Repository
[https://github.com/sydferns/final-project.git ](https://github.com/sydferns/final-project.git)

## Description
I plan to make a tower stack game. The blocks move at the top of the screen and the user then clicks in an attempt to stack them.


## Features
- Feature 1: Blocks move from one side to the other, and vice versa on the screen.
	- Block will move along x axis coordinates by adding/subtracting the number to move along to. 
- Feature 2: Click to drop block.
	- User will mouse click to drop box on to the stack. Will have to implement code for mouse clicks.
- Feature 3: Screen moves upward with every stack
	- The images will go along the y-axis and out of frame after determined point. Out of frame graphics will be deleted to remove lag.
- Feature 4: Excess block cuts off
	- Will measure distance the blocks overlap on and remove excess using loops.
- Feature 5: Display text/ numbers to show score.
  - Will show words like "perfect" for correct stacks or "miss" and "game over" if failed.

## Challenges
- Will have to research mouse click functions and options
- will have to research how to move frame upwards
- How to remove off the excess of the block and reduce size of incoming blocks.

## Outcomes
Ideal Outcome:
- Blocks move on the top of the screen from left to right and vice versa. Upon clicking with a mouse, the block falls.
- If block lands correctly on a designated base, user scores point. Words or scores will show up based on accuracy.
- Blocks will continue to stack until user misses or decides to quit. Blocks may get faster as tower grows taller.
- If user places block partially, the excess block gets cut off and the incoming block size reduces.

Minimal Viable Outcome:
- For bare essential, blocks move left to right on the screen and fall when user clicks with a mouse.
- Blocks are able to stack until user misses or quits.

## Milestones

- Week 1
  1. Create a background screen.
  2. Create a base
  3. Block moves left to right and vice versa.

- Week 2
  1. Mouse clicks drops block
  2. If block falls in wrong spaces words appear on screen

- Week N (Final)
  1. Block cuts off extra over hang
  2. Some minor design changes to personalize game
  3. game test runs smoothly
