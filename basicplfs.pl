% Kevin Kovacik

% xreverse function: reverses a list via iterating through list recursively and appends each element to a new list in reverse order
% base case
xreverse([], []).

% main
xreverse([A|LO], LR) :-
    xreverse(LO, N),
    append(N, [A], LR).

% xunique function: uses helper function xunique2 to generate list of unique elements 
xunique(L, R) :-
    xunique2(L, [], R).
	
% xunique2 function: takes in a list iterates through it, checks if the current element is a member of the accumulator, 
% if so move to next element, if not, add element to accumulator.
% base case
xunique2([], A, N) :-
    reverse(A, N).

% main	
xunique2([H|T], A, R) :-
    member(H, A),
    xunique2(T, A, R).
	
xunique2([H|T], A, R) :-
    xunique2(T, [H|A], R).

% xdiff function: uses the built-in function subtract to remove the elements L1 has in common with L2 to produce R; (L1-L2)
xdiff(L1,L2,R) :-
    subtract(L1,L2,R).
	
% removeLast function: recursively iterates through a list (arg1) until it gets to the last element at which point it returns the  last element (Last) and a list with out the last element ([H|R]).
removeLast([E|[]], [], E).

removeLast([H|T], [H|R], Last) :-
    removeLast(T, R, Last).

% clique function: an aggregate function which effectively determines if a subset is a cliqu
clique(L) :- 
    findall(X,node(X),Nodes), 
    xsubset(L,Nodes), 
    allConnected(L).

% xsubset function: function which returns True if ([X|Xs]) is a subset of (Set).
xsubset([], _).

xsubset([X|Xs], Set) :- 
    xappend(_, [X|Set1], Set), xsubset(Xs, Set1).

% xappend
xappend([], L, L).

xappend([H|T], L, [H|R]) :- 
    xappend(T, L, R).

% allConnected: using helper function 'connect', allConnected determines whether a node is connected to all other nodes.  
allConnected([]).

allConnected([Node|L]) :-
    connect(Node, L),
    allConnected(L).

% connect function: returns True if a given node is connected to all other nodes
connect(_, []).

connect(N, [H|T]) :-
    (edge(N, H); edge(H, N)), 
    connect(N, T).
