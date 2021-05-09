# Exceptions module
from automathon.errors.errors import *
from collections import deque
from graphviz import Digraph
from automathon.finiteAutomata.dfa import DFA

class NFA():
  """A Class used to represent a Non-Deterministic Finite Automaton

  ...

  Attributes
  - - - - - - - - - - - - - - - - - -
  Q : set
    Set of strings where each string represent the states.
    Ex:
      Q = {'q0', 'q1', 'q2'}

  sigma : set
    Set of strings that represents the alphabet.
    Ex:
      sigma = {'0', '1'}
  
  delta : dict
    Dictionary that represents the transition function.
    Ex:
      delta = {
                'q0' : {
                        '0' : ['q0', 'q2'],
                        '1' : ['q1', 'q2', 'q3']
                       },
                'q1' : {
                        '0' : ['q2'],
                        '1' : ['q0', 'q1']
                       },
                'q2' : {
                        '0' : ['q1', 'q2'],
                        '' : ['q2']
                       },
              }
  
  initialState : str
    String that represents the initial state from where any input is processed (initialState ∈ Q / initialState in Q).
    Ex:
      initialState = 'q0'
  
  F : set
    Set of strings that represent the final state/states of Q (F ⊆ Q).
    Ex:
      F = {'q0', 'q1'}
  

  Methods
  - - - - - - - - - - - - - - - - - -

  isValid() -> bool : Returns True if the NFA is a valid automata
  accept(S : str) -> bool : Returns True if the given string S is accepted by the NFA
  complement() -> NFA : Returns the complement of the NFA
  """

  def __init__(self, Q : set, sigma : set, delta : dict, initialState : str, F : set):
    """
    Parameters
    - - - - - - - - - - - - - - - - - -
    
    Q : set
      Set of strings where each string represent the states.
    
    sigma : set
      Set of strings that represents the alphabet.
    
    delta : dict
      Dictionary that represents the transition function.
    
    initialState : str
      String that represents the initial state from where any input is processed (initialState ∈ Q / initialState in Q).
    
    F : set
      Set of strings that represent the final state/states of Q (F ⊆ Q).
    """
    self.Q = Q
    self.sigma = sigma
    self.delta = delta
    self.initialState = initialState
    self.F = F

  def accept(self, S : str) -> bool:
    """ Returns True if the given string S is accepted by the NFA

    The string S will be accepted if ∀a · a ∈ S ⇒ a ∈ sigma, which means that all the characters in S must be in sigma (must be in the alphabet).

    Parameters
    - - - - - - - - - - - - - - - - - -
    S : str
      A string that the NFA will try to process.
    """

    ## Basic Idea: Search through states (delta) in the NFA, since the initial state to the final states

    ## BFS states

    q = deque() ## queue -> states from i to last character in S | (index, state)
    q.append( [0, self.initialState] ) ## Starts from 0
    ans = False ## Flag

    while q and not ans:
      frontQ = q.popleft()
      idx = frontQ[0]
      state = frontQ[1]

      if idx == len(S):
        if state in self.F:
          ans = True
      elif S[idx] not in self.sigma:
        raise InputError(S[idx], 'Is not declared in sigma')
      elif state in self.delta:
        ## Search through states
        for transition in self.delta[state].items():
          d = transition[0]
          states = transition[1]

          if d == "":
            ## Is epsilon
            for state in states:
              #Do not consume character
              q.append( [idx, state] )
          elif S[idx] == d:
            for state in states:
              #Consume character
              q.append( [idx+1, state] )

    if S == "":
      ans = True

    return ans


  def isValid(self) -> bool:
    """ Returns True if the NFA is an valid automata """

    #Validate if the initial state is in the set Q
    if self.initialState not in self.Q:
      raise SigmaError(self.initialState, 'Is not declared in Q')

    #Validate if the delta transitions are in the set Q
    for d in self.delta:
      if d != "" and d not in self.Q:
        raise SigmaError(d, 'Is not declared in Q')

        #Validate if the d transitions are valid
        for s in self.delta[d]:
          if s != "" and s not in self.sigma:
            raise SigmaError(s, 'Is not declared in sigma')
          for q in self.delta[d][s]:
            if q not in self.Q:
              raise SigmaError(self.delta[d][s], 'Is not declared Q')


    #Validate if the final state are in Q
    for f in self.F:
      if f not in self.Q:
        raise SigmaError(f, 'Is not declared in Q')

    #None of the above cases failed then this NFA is valid
    return True

  def complement(self) -> 'NFA':
    """Returns the complement of the NFA."""
    Q = self.Q
    sigma = self.sigma
    delta = self.delta
    initialState = self.initialState
    F = { state for state in self.Q if state not in self.F}
    
    return NFA(Q, sigma, delta, initialState, F)
  
  def getEClosure(self, q):
    ans = [q]

    if q in self.delta:
      if '' in self.delta[q]:
        for st in self.delta[q]['']:
          ans.extend([k for k in self.getEClosure(st) if k not in ans])
    return ans

  def removeEpsilonTransitions(self) -> 'NFA':
    """Returns a copy of the actual NFA that doesn't contain epsilon transitions"""

    Qprime = []
    deltaPrime = dict()

    eClosures = []

    isolatedNodes = []

    tmp = self.getEClosure(self.initialState)
    qVisiteds = tmp

    if len(tmp) == 1:
      isolatedNodes.extend(tmp.copy())
    elif len(tmp) > 1:
      eClosures.append(tmp.copy())

    for q in self.Q:
      tmp = []
      if q not in qVisiteds:
        tmp = self.getEClosure(q)
      qVisiteds.extend([k for k in tmp if k not in qVisiteds])
      if len(tmp) == 1:
        isolatedNodes.extend(tmp.copy())
      elif len(tmp) > 1:
        eClosures.append(tmp.copy())
    
    ## MarkClosures
    nodeClosure = dict()
    valueClosure = dict()
    cnt = 0

    for c in isolatedNodes:
      cnt += 1
      nodeClosure[c] = cnt
      valueClosure[cnt] = [c]
      Qprime.append([c])

    for c in eClosures:
      cnt += 1
      for e in c:
        if e in nodeClosure:
          Qprime.remove([e])
        nodeClosure[e] = cnt
      valueClosure[cnt] = c
      Qprime.append(c)

    auxDelta = dict()
    for qs in Qprime: ## Qprime = [ [], [], ...]
      ##Iterate over the states
      auxDelta[str(qs)] = dict() ##Initialize the auxiliar delta
      for transitionValue in self.sigma:
        ## get the values
        if transitionValue != '':
          visited = []
          auxDelta[str(qs)][transitionValue] = []
          for q in qs:
            if q in self.delta and transitionValue in self.delta[q]:
              for s in self.delta[q][transitionValue]:
                if nodeClosure[s] not in visited:
                  visited.append(nodeClosure[s])
                  auxDelta[str(qs)][transitionValue].append(nodeClosure[s])
    
    for qs in auxDelta:
      deltaPrime[qs] = dict()
      for transitionValue in auxDelta[qs]:
        deltaPrime[qs][transitionValue] = []
        for idValue in auxDelta[qs][transitionValue]:
          deltaPrime[qs][transitionValue].append( str(valueClosure[idValue]) )

    finalStates = set()
    for qs in Qprime:
      for q in qs:
        if q in self.F:
          finalStates.add(str(qs))
          break
    
    initialState = []
    for qs in valueClosure[nodeClosure[str(self.initialState)]]:
      initialState.append(qs)
    
    aux = set()
    for qs in Qprime:
      aux.add(str(qs))

    return NFA(Qprime, self.sigma, deltaPrime, str(initialState), finalStates)

  def getDFA(self) -> DFA:
    """Convert the actual NFA to DFA and return it's conversion"""

    ##verify if have epsilon transitions
    for q in self.Q:
      if q in self.delta:
        for transitionValue in self.delta[q]:
          if transitionValue == '':
            return self.removeEpsilonTransitions()

    Qprime = []
    deltaPrime = dict()

    queue = deque()
    visited = [[self.initialState]]
    queue.append([self.initialState])

    while queue:
      qs = queue.pop() ## state Q

      T = dict() ## {str : list}

      for q in qs:
        if q in self.delta:
          for s in self.delta[q]:
            tmp = self.delta[q][s].copy()
            if s in T:
              ## avoid add repeated values
              T[s].extend( [k for k in tmp if k not in T[s]] )
            else:
              T[s] = tmp
      
      for t in T:
        T[t].sort()
        tmp = T[t].copy()
        if tmp not in visited:
          queue.append(tmp)
          visited.append(tmp)
        T[t] = str(T[t])
      
      deltaPrime[str(qs)] = T
      Qprime.append(qs)
    
    Fprime = set()

    for qs in Qprime:
      for q in qs:
        if q in self.F:
          Fprime.add(str(qs))
          break
    
    aux = set()

    
    for qs in Qprime:
      aux.add(str(qs))
    
    Qprime = aux
    
    return DFA(Qprime, self.sigma, deltaPrime, str([self.initialState]), Fprime)

  def view(self, fileName: str):
    dot = Digraph(name=fileName, format='png')
    
    dot.graph_attr['rankdir'] = 'LR'

    dot.node("", "", shape='plaintext')

    for f in self.F:
      dot.node(f, f, shape='doublecircle')
    
    for q in self.Q:
      if q not in self.F:
        dot.node(q, q, shape='circle')
    
    dot.edge("", self.initialState, label="")
    
    for q in self.delta:
      for s in self.delta[q]:
        for t in self.delta[q][s]:
          if s == '':
            dot.edge(q, t, label='ε')
          else:
            dot.edge(q, t, label=s)
    
    dot.render()