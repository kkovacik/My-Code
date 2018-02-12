:- use_module(library(clpfd)).

disarm([], [], []).

disarm(Adivs, Bdivs, Sol) :-
    select(A,Adivs,L1), select(B,L1,L2),
    select(C,Bdivs,L3),
    D1 = [A,B],
    D2 = [C],
    A + B #= C,
    disarm(L2, L3, S),
    M = [D1,D2], 
    append([M], S, Sol).

disarm(Adivs, Bdivs, Sol) :-
    select(A,Bdivs,L1), select(B,L1,L2),
    select(C,Adivs,L3),
    D1 = [C],
    D2 = [A,B],
    A + B #= C,
    disarm(L2, L3, S),
    M = [D1,D2], 
    append([M], S, Sol).

