# Reinforcement_Learning-PacMan
Code of reinforcement learning agent learning to play pacman game. A part of exercises in berkley university's course on .

NOTE : While the code to extract information from pacman environment and other auxillary methods such as state and action definitions were already provided in the code by Berkley course work team, the essential and important functions tpo implement reinforcement learning such as computing the values, action values, performing action selection and implementing RL algorithms are written by the author (Hari Teja) himself.  

This code is a complete algorithmic implementation of Q-learning and MDP's for gridworld and pacman game.
Detailed description of the problem and objectives can be found in " http://ai.berkeley.edu/reinforcement.html#Q1 "

For self-learning PacMan implementation :
  1. For small gridworld of pacman, type in the terminal " python pacman.py -p PacmanQAgent -x 2000 -n 2010 -l smallGrid " 
  2. For larger grid and implementation of approximate agent instead of explicit state space representation, type 
  " python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 60 -l mediumClassic "  
