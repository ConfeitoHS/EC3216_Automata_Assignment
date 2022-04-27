#
#  Automata Programming Assignment #1 - 1
#
#  Name: ConfeitoHS
#  ID: 20215---
#

import sys


def pa1_1(str_automata, str_input,verbose):
    """Programming Assignment 1-1 (read document).

    :param str_automata: A string which defines an automata.
    :param str_input: Input string.
    :return: str_output: "accept" or "reject".
    """
    # Parser
    FA = str_automata.split('\n')
    meta = list(map(int,FA[0].split()[1:]))
    n_states = meta[0]
    n_finals = meta[2]
    n_syms = meta[3]
    n_rules = meta[4]

    # Parse States
    states = FA[1].split()
    st2no = dict(zip(states,range(n_states)))   # state name to index
    initial = st2no[FA[2].split()[0]]   # initial state (in index)
    finals = [st2no[st] for st in FA[3].split()]    # accept states (in index)

    # Parse Symbols
    syms = ['_']+FA[4].split()  # characters with lambda
    sym2no = dict(zip(syms, range(n_syms+1)))   # symbol to index

    # Parse Transitions
    delta = [[0]*(n_syms+1) for _ in range(n_states)]   # delta[from][symbol] = (set of states)
    for rule in FA[5:]:
        if not rule:
            break
        rule = rule.split()
        fr = st2no[rule[0]]
        ch = sym2no[rule[1]]
        to = st2no[rule[2]]
        # set of states is stored in bit notation that indicates 
        delta[fr][ch] |= (1<<to)
    
    if(verbose):
        print("\n--- TRANSITION ---")
        print(f"|{'State':^5}|",end='')
        for c in syms:
            print(f"{c:^10}|",end='')
        print()
        for i,d in enumerate(delta):
            print("|",end='')
            print(f"{states[i]:^5}|",end='')
            for k in range(n_syms+1):
                sts = []
                for t in range(n_states):
                    if d[k] & (1 << t):
                        sts.append(states[t])
                print(f"{','.join(sts):^10}|",end='')
            print()

    # Build lambda closure cache for all states
    lclosure = []
    for st in range(n_states):
        visit = 0
        stacks = [st]
        # DFS
        while len(stacks)>0:
            v = stacks.pop()
            if visit & (1<<v) == 0:
                if v < len(lclosure): # reuse calculated before if possible
                    visit |= lclosure[v]
                else:   # or not, continue
                    visit |= (1<<v)
                    for i in range(n_states):
                        if delta[v][0] & (1<<i): # if lambda trans of v has i th node
                            stacks.append(i)
        
        # marked 
        lclosure.append(visit)
    
    if(verbose):
        print("\n--- Lambda Closures ---")
        print(f"|{'State':^10}|{'result':^15}|",end='')
        print()
        for i,d in enumerate(delta):
            print("|",end='')
            print(f"{states[i]:^10}|",end='')
            sts = []
            for t in range(n_states):
                if lclosure[i] & (1 << t):
                    sts.append(states[t])
            print(f"{','.join(sts):^15}|",end='')
            print()
        print()

    # Start Automata
    # state to {state}, do lambda closure at initial state
    current = lclosure[initial]
    if(verbose):
        sts =[]
        for t in range(n_states):
            if lclosure[initial] & (1 << t):
                sts.append(states[t])
        print(f"lambda({states[initial]}) = {{{','.join(sts)}}}")
    for ch in str_input.strip():

        ch = sym2no[ch]
        # transition
        temp = 0
        for i in range(n_states):
            if current & (1<<i):
                temp |= delta[i][ch]

        # do lambda closure
        current = 0
        for i in range(n_states):
            if temp & (1<<i):
                current |= lclosure[i]
        if(verbose):
            #Debug
            print(f"lambda(Move({{{','.join(sts)}}},{syms[ch]})) = ",end='')
            sts =[]
            for t in range(n_states):
                if temp & (1 << t):
                    sts.append(states[t])
            print(f"lambda({{{','.join(sts)}}}) = ",end='')
            sts =[]
            for t in range(n_states):
                if current & (1 << t):
                    sts.append(states[t])
            print(f"{{{','.join(sts)}}}")
    # Check if final transition set includes final state
    accepts = False
    for f in finals:
        if current & (1<<f):
            accepts = True
    if(verbose):
        print("\nAccept\n" if accepts else "\nReject\n")
    return "accept" if accepts else "reject"


def main(*args):
    """File IO. Do not modify this function!"""
    if len(args) < 4:
        raise ValueError("Not enough arguments!")

    filename1 = args[1]
    filename2 = args[2]
    with open(filename1, "r") as fp1:
        text1 = fp1.read()
    with open(filename2, "r") as fp2:
        text2 = fp2.read()
    deb = True if len(args) == 4 else False
    text3 = pa1_1(text1, text2,deb)

    filename3 = args[3]
    with open(filename3, "w") as fp3:
        fp3.write(text3)


if __name__ == '__main__':
    args = sys.argv
    main(*args)
