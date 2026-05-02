pos_to_rc(Pos, R, C) :-
    R is (Pos - 1) // 6,
    C is (Pos - 1) mod 6.

rc_to_pos(R, C, Pos) :-
    Pos is R * 6 + C + 1.

move(X, Y) :-
    pos_to_rc(X, R, C),
    (
        R1 is R+2, C1 is C+1;
        R1 is R+2, C1 is C-1;
        R1 is R-2, C1 is C+1;
        R1 is R-2, C1 is C-1;
        R1 is R+1, C1 is C+2;
        R1 is R+1, C1 is C-2;
        R1 is R-1, C1 is C+2;
        R1 is R-1, C1 is C-2
    ),
    R1 >= 0, R1 < 6,
    C1 >= 0, C1 < 6,
  rc_to_pos(R1, C1, Y).

single_move(X, Y) :-
    move(X, Y), !.

two_path(X, Y) :-
    move(X, Z),
    move(Z, Y),
    X \= Y.

three_path(X, Y) :-
    move(X, A),
    move(A, B),
    move(B, Y),
    X \= Y. 

