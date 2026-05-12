# Block Tower Stack

## Demo
Demo Video:

## GitHub Repository
GitHub Repo: https://github.com/sydferns/final-project.git

## Overview
Block Tower Stack is a simple stacking game built using Python and Pygame. The main objective is to stack the moving blocks as accurately as possible on top of each other to build the tallest tower possible. It starts with a base and each new block that drops becomes the new base for the next one. The game continues till the player either misses the platform or quits. 

The design for the game is minimalistic visually, but focuses instead on timing and precision of the player.

## Structure
The src folder contains the code for the game. It contains the entire game logic including:
- The Box class, which defines the blocks shape, movement and behavior.
- Placement logic for blocks to stack.
= Game management (start screen, gameplay, and game over screen)
- Camera movement to follow the rising tower
- Score tracking system.
- The main game loop.

The game is small in scope so all code is in one file for simplicity. The code is structured into logical sections for readability. The proposal.md file contains the project proposal. 

## Design Considerations
The game was designed to be simple and minimalistic so as to be relaxing to the player and a respite from daily life hustle. The core of the game is intentionally easy to understand relying on timing. The physics used are simple to maintain clarity.

A key design feature was to use a camera system that follows the current stack blocks. The camera gives an illusion of the tower rising while maintaining focus on the active block and keeping it centered.

## Future Improvements
There are many ways the project could be improved upon in the future:
- Making the game more visually appealing.
- Physics enhancements: Adding wind or obstacles that fly in the screen randomly could make the game mroe challenging.
- Sound effects or music: would improve the game feel and make it more immersive.
- Difficulty: Increasing block speed would make the game more challenging to try.
As the project grows with these improvements, splitting the project into multiple files would improve maintainability.

