# Automathon

Created by: Robin Hafid Quintero Lopez

[![Build Status](https://travis-ci.com/rohaquinlop/automathon.svg?branch=main)](https://travis-ci.com/rohaquinlop/automathon)

A Python library for simulating and visualizing finite automata.

## Links
- GitHub repository: https://github.com/rohaquinlop/automathon
- PyPI: https://pypi.org/project/automathon/
- Twitter: https://twitter.com/RobinHafid
- Contact: rohaquinlop301@gmail.com

## Installation

### PyPI
```Python
pip install automathon
```

You also need to install Graphviz on your computer ([download page](https://www.graphviz.org/download/), [installation procedure for Windows](https://forum.graphviz.org/t/new-simplified-installation-procedure-on-windows/224), [archived versions](https://www2.graphviz.org/Archive/stable/)).

Make sure that the directory containing the **dot** executable is on your systems’ path.

## Upgrade

### PyPI
```Python
pip install automathon --upgrade
```

## Deterministic Finite Automata

![DFA Visualization](https://lh3.googleusercontent.com/fife/ABSRlIoeWTAicQSJA8qaVaVfz1oRENPSyp4O_qo29zptk9BumRx-t1FYVaRtVeM2lgoY7CpRbgzUUnWb62qi63TZUkB6Okht7qNG1iK_DpIcVxz7sgLM9Ysyue3WSnwvG55Oxe6BG--_dqplScQkbSq9TscYq5ThFjrTl6yBTBQEz2ZK1Y4CMfrIeBmnXswlwyshKrVRqmjv-TZSnc1lp_Age-kZlcizL3Kf2E9rD02NgQYwWqd6JbWXXDCv1DPWTZ8J1VkZpoC0XwN1eEdYC2PrgoSU-KqWrr-Ih5e3JMxojdgSgiocRMQx3lyitnD51dw3AcDrdYVSQUqxCEID3MZ3wj6wTb-uSK3-r6yHJsq_ObXQOfdQP69myEDzg7lXHEANUN_1TGYa58W3rI9PXC-DL9k5Vt_KbUoJrMhF76dASOodl_bzKn4hBhTmGty9Culu9wyaNFNMauGSSv5VnBP8OHI_Mslg9SgkX5aZ1yZhVAgzvyrPTEfLIXyLwGY0nAfmxmQUzfeeV3xLwV5Y6Xf7tTfRL0YNNUo7it2IQrpDQxsXx77i-xNVdRSUKceS10nMQZ4UZav-3R91_J3zChbgxvQOOPyR_jGmiVzDu6djLyQw9ZFhG9J45nEuHdtVmyDbh6MzWO8rOUBPjPaDbUYOdY-dzi6dTYV5UPgl57etP_Dkph3eIv5OuipqdeJfLqRJCKxoJ1RsXMe2MqlLdOcSgjtYleuXrbT_VDc=w1514-h772-ft)

### Representing the previous automata

```Python
from automathon import DFA
Q = {'q0', 'q1', 'q2'}
sigma = {'0', '1'}
delta = { 'q0' : {'0' : 'q0', '1' : 'q1'},
          'q1' : {'0' : 'q2', '1' : 'q0'},
          'q2' : {'0' : 'q1', '1' : 'q2'}
        }
initialState = 'q0'
F = {'q0'}

automata1 = DFA(Q, sigma, delta, initialState, F)
## This is an example about creating a DFA with the library
```

### Verify if the automata is valid

```python
automata1.isValid()   #True
```

### Verify if the automata accept a string

```python
automata1.accept("001001")   #True
automata1.accept("00100")    #False
```

### Get the automata's complement

```python
notautomata1 = automata1.complement()
notautomata1.accept("00100")    #True
```

### Visualize the automata

For both, DFA and NFA, the view method enables to visualize the automaton, receives as parameter a String as the file name for the png and svg files.

![DFA Visualization](https://lh3.googleusercontent.com/fife/ABSRlIoeWTAicQSJA8qaVaVfz1oRENPSyp4O_qo29zptk9BumRx-t1FYVaRtVeM2lgoY7CpRbgzUUnWb62qi63TZUkB6Okht7qNG1iK_DpIcVxz7sgLM9Ysyue3WSnwvG55Oxe6BG--_dqplScQkbSq9TscYq5ThFjrTl6yBTBQEz2ZK1Y4CMfrIeBmnXswlwyshKrVRqmjv-TZSnc1lp_Age-kZlcizL3Kf2E9rD02NgQYwWqd6JbWXXDCv1DPWTZ8J1VkZpoC0XwN1eEdYC2PrgoSU-KqWrr-Ih5e3JMxojdgSgiocRMQx3lyitnD51dw3AcDrdYVSQUqxCEID3MZ3wj6wTb-uSK3-r6yHJsq_ObXQOfdQP69myEDzg7lXHEANUN_1TGYa58W3rI9PXC-DL9k5Vt_KbUoJrMhF76dASOodl_bzKn4hBhTmGty9Culu9wyaNFNMauGSSv5VnBP8OHI_Mslg9SgkX5aZ1yZhVAgzvyrPTEfLIXyLwGY0nAfmxmQUzfeeV3xLwV5Y6Xf7tTfRL0YNNUo7it2IQrpDQxsXx77i-xNVdRSUKceS10nMQZ4UZav-3R91_J3zChbgxvQOOPyR_jGmiVzDu6djLyQw9ZFhG9J45nEuHdtVmyDbh6MzWO8rOUBPjPaDbUYOdY-dzi6dTYV5UPgl57etP_Dkph3eIv5OuipqdeJfLqRJCKxoJ1RsXMe2MqlLdOcSgjtYleuXrbT_VDc=w1514-h772-ft)
```Python
automata1.view("DFA Visualization")
```

### Convert DFA to NFA

If you need to use a DFA and operate with a NFA you can convert your DFA to NFA class, using the function **getNFA**. **getNFA** convert your DFA to NFA class and returns its conversion.

```python
automata1NFA =  automata1.getNFA()
automata1NFA.view("DFA to NFA")
```

### Product of two automatas
The **product** function receives a DFA and  returns the product of two DFAs, your actual DFA and the given as parameter.

```python
Q = {'A', 'B'}
sigma = {'0', '1'}
delta = {
          'A' : {
                  '0' : 'A',
                  '1' : 'B'
                 },
          'B' : {
                  '0' : 'B',
                  '1' : 'A'
                 }
        }
initialState = 'A'
F = {'B'}
dfa = DFA(Q, sigma, delta, initialState, F)

Q1 = {'R', 'S', 'T', 'U'}
sigma1 = {'0', '1'}
delta1 = {
          'R' : {
                  '0' : 'S',
                  '1' : 'R'
                },
          'S' : {
                  '0' : 'T',
                  '1' : 'R'
                },
          'T' : {
                  '0' : 'U',
                  '1' : 'R'
                },
          'U' : {
                  '0' : 'U',
                  '1' : 'U'
                }
        }
initialState1 = 'R'
F1 = {'U'}

dfa1 = DFA(Q1, sigma1, delta1, initialState1, F1)

dfa2 = dfa.product(dfa1)

assert dfa2.isValid() == True
assert dfa2.accept("0001") == True
assert dfa2.accept("00010010") == False
```

### Union of two automatas
The **union** function receives a DFA and returns the union of two DFAs, your actual DFA and the given as parameter.

```python
Q = {'A', 'B'}
sigma = {'0', '1'}
delta = {
          'A' : {
                  '0' : 'A',
                  '1' : 'B'
                 },
          'B' : {
                  '0' : 'B',
                  '1' : 'A'
                 }
        }
initialState = 'A'
F = {'B'}
dfa = DFA(Q, sigma, delta, initialState, F)

Q1 = {'R', 'S', 'T', 'U'}
sigma1 = {'0', '1'}
delta1 = {
          'R' : {
                  '0' : 'S',
                  '1' : 'R'
                },
          'S' : {
                  '0' : 'T',
                  '1' : 'R'
                },
          'T' : {
                  '0' : 'U',
                  '1' : 'R'
                },
          'U' : {
                  '0' : 'U',
                  '1' : 'U'
                }
        }
initialState1 = 'R'
F1 = {'U'}

dfa1 = DFA(Q1, sigma1, delta1, initialState1, F1)

dfa2 = dfa.union(dfa1)

assert dfa2.accept("00010010") == True
assert dfa2.accept("0011000") == True
assert dfa.isValid() == True
```

## Non-Deterministic Finite Automata
![](http://www.r9paul.org/wp-content/uploads/2008/12/nfa_example.jpg)

Image taken from: http://www.r9paul.org/blog/2008/nondeterministic-finite-state-machine/

### Representing the previous automata

```Python
from automathon import NFA

## Epsilon Transition is denoted by '' -> Empty string
Q = {'q1', 'q2', 'q3', 'q4'}
sigma = {'0', '1'}
delta = {
          'q1' : {
                  '0' : {'q1'},
                  '1' : {'q1', 'q2'}
                  },
          'q2' : {
                  '0' : {'q3'},
                  '' : {'q3'}
                  },
          'q3' : {
                  '1' : {'q4'},
                  },
          'q4' : {
                  '0' : {'q4'},
                  '1' : {'q4'},
                  },
        }
initialState = 'q1'
F = {'q4'}

automata2 = NFA(Q, sigma, delta, initialState, F)
## This is an example about creating a NFA with the library
```

### Verify if the automata is valid

```python
automata2.isValid()   #True
```

### Verify if the automata accept a string

```python
automata2.accept("0000011")   #True
automata2.accept("000001")    #False
```

### Get the automata's complement

```python
notautomata2 = automata1.complement()
notautomata2.accept("000001")    #True
```

### Visualize the automata

![NFA Visualization](https://lh3.googleusercontent.com/fife/ABSRlIoyNVLUsLV1nkvolj1PMNdI0dGOU2jAMDsiNxq-V7h26Qgor71kn5hYGEcqoV54Iebftdgt5pBb7wP49f0SDBfGr0oegUOZG9u9Ud34JON17RqMVVVkb9Di2UDYqUbRLbuqCXskIBWnj4hfX4fV3XHqORgnn_Qsci9USWvMRkvNEsU1qLkXfMUJCLFc07ABWs-EdJIPU6FGW_gG87NHdr8sPwotZ3DEms1uz4DEizDk278Dr57s8SzOys_1Kz3h7gTR1_CliYGl4ZD1y69dFf_2e2OTydmn2P4y4o8DULKQixDGkZLws-ATi1bQzSjEZxMWlW-PLkHdfF1KTc7I-QVhczQiuVs5KLoE5bK0u7YjtZFR3XyjpGS2_Q8yB3j6ggqUqt1uGNHUntOTPqye0krtyWt10YjbtXTeSjWW4i18mXY1SA-iZu9KTH5IdEttbWoYyfAQdJA4trz5ZyEhUjwwo-peaO8wIc_8xlRY0orrvduOtx_AnqtjOK_QwCdFpVjBzEygxR_z4RRDreOLlLITeOSwROwbbtGe9oYT2skyX0H_j8-pGaMabUnJ4eyDviPTa5bEZk0B5LoKa-hdDBkjTYX-zDCHg1xGsXHWLyMQtvvuBP1ptCJhODgWrmdCyfsw3UbOmfpusUW_US1E3OXsKwtAsH17bXTyyQGEeHjgiBAwH9-Tdf-l1bcRNzR9SEhYdUFtFAvYlFf4pBKbkgTe-DgIDQ_zIjA=w959-h772-ft)
```Python
automata2.view("NFA Visualization")
```

### Remove Epsilon transitions from NFA

```python
automata3 = automata2.removeEpsilonTransitions()
automata3.view("NFA without EpsilonTransitions")
```

### Convert NFA to DFA

```python
automata4 = automata3.getDFA()
automata4.view("NFA to DFA")
```

### Product of two automatas
The **product** function receives a NFA and returns the product of two NFAs, your actual NFA and the given as parameter.

```python
Q = {'A', 'B'}
sigma = {'a', 'b'}
delta = {
  'A' : {
    'a' : {'B'},
    'b' : {'A'}
  },
  'B': {
    'a': {'A'},
    'b': {'B'}
  }
}
initialState = 'A'
F = {'A'}

nfa = NFA(Q, sigma, delta, initialState, F)

Q1 = {'C', 'D'}
sigma1 = {'a', 'b'}
delta1 = {
  'C': {
    'a' : {'C'},
    'b' : {'D'}
  },
  'D': {
    'a' : {'D'},
    'b' : {'C'}
  }
}
initialState1 = 'C'
F1 = {'C'}

nfa1 = NFA(Q1, sigma1, delta1, initialState1, F1)

nfa2 = nfa.product(nfa1)

assert nfa2.isValid() == True
assert nfa2.accept('') == True
assert nfa2.accept('bb') == True
assert nfa2.accept('b') == False
assert nfa2.accept('bbaa') == True
assert nfa2.accept('bbaaa') == False
```

### Union of two automatas
The **union** function receives a NFA and returns the union of two NFAs, your actual NFA and the given as parameter.

```python
Q = {'A'}
sigma = {'a'}
delta = {
  'A' : {
    'a' : {'A'}
  }
}
initialState = 'A'
F = {'A'}
nfa = NFA(Q, sigma, delta, initialState, F)

Q1 = {'C', 'D', 'E'}
sigma1 = {'a', 'b'}
delta1 = {
  'C' : {
    'b' : {'D'},
  },
  'D': {
    'a' : {'E'},
    'b' : {'D'}
  }
}

initialState1 = 'C'
F1 = {'E'}

nfa1 = NFA(Q1, sigma1, delta1, initialState1, F1)

nfa2 = nfa.union(nfa1)

assert nfa2.isValid() == True
assert nfa2.accept("aaaaaa") == True
assert nfa2.accept("aaaabbbbaaa") == False
assert nfa2.accept("bbbbbbbbba") == True
assert nfa2.accept("aaaaaaaab") == False
```

## Errors

Errors that can be returned during the execution, and the cases that can appear.

- **SigmaError**:
  - The automata contain an initial state, or a final state that's not defined on Q.
  - The automata contain a delta transition that's not defined on Q or in Sigma.

- **InputError**:
  - The automata is trying to consume a letter that's not defined in sigma.
