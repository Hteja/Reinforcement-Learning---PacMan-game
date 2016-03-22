# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        state_set = self.mdp.getStates()
        state_size = len(state_set)
        iter_count = self.iterations
        while iter_count > 0:
            for i in range(0, state_size):
                cur_state = state_set[i]
                pos_actions = self.mdp.getPossibleActions(cur_state)
                summ = [0]*len(pos_actions)
                if len(pos_actions) == 0:
                    summ = 0
                    R = self.mdp.getReward(cur_state, [], cur_state)
                    sigma = (R+(self.discount*self.values[cur_state]))
                    summ = summ+sigma
                else:
                    for j in range(0, len(pos_actions)):
                        action = pos_actions[j]
                        transit_list = self.mdp.getTransitionStatesAndProbs(cur_state, action)                            
                        # [(nex_states, state_probs)] = mdp.getTransitionStatesAndProbs(cur_state, j)
                        k_len = len(transit_list) 
                        for k in range(0, k_len):   
                            nex_state = transit_list[k][0]
                            state_prob = transit_list[k][1]
                            R = self.mdp.getReward(cur_state, action, nex_state)                                                     
                            sigma = state_prob*(R+(self.discount*self.values[nex_state]))
                            summ[j] = summ[j]+sigma
                if self.mdp.isTerminal(cur_state) == 0:
                    self.values[cur_state] = max(summ)
            iter_count = iter_count-1

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        transits = self.mdp.getTransitionStatesAndProbs(state, action)
        summ = 0
        for i in range(0, len(transits)):
            nex_state = transits[i][0]
            state_prob = transits[i][1]
            R = self.mdp.getReward(state, action, nex_state)
            if self.mdp.isTerminal(nex_state) == 0:
                V_next = self.discount*self.values[nex_state]
            else:
                V_next = 0
            sigma = state_prob*(R+V_next)
            summ = summ+sigma
        Q_val = summ
        return Q_val          
        util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        pos_actions = self.mdp.getPossibleActions(state)
        max_action = ()
        summ = [0]*len(pos_actions)
        if self.mdp.isTerminal(state) == 1:
            return None
        for ii in range(0, len(pos_actions)):
            action = pos_actions[ii]
            transit_list = self.mdp.getTransitionStatesAndProbs(state, action)
            # [(nex_states, state_probs)] = mdp.getTransitionStatesAndProbs(cur_state, j)
            k_len = len(transit_list) 
            for k in range(0, k_len):   
                nex_state = transit_list[k][0]
                state_prob = transit_list[k][1]
                R = self.mdp.getReward(state, action, nex_state)
                V_nex = self.values[nex_state]
                sigma = state_prob*(R+(self.discount*V_nex))
                summ[ii] = summ[ii]+sigma
        max_action = pos_actions[summ.index(max(summ))]
        return max_action
        util.raiseNotDefined()
        

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
