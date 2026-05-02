  parent(ram, priya).
  parent(ram, rohit).
  parent(sita, priya).
  parent(sita, rohit).
  parent(sita, pooja).

  male(rohit).

  female(sita).
  female(priya).
  female(pooja).

  sibling(X, Y) :-
      parent(P, X),
      parent(P, Y),
      X \= Y.

  brother(X, Y) :-
      sibling(X, Y),
      male(X).

  sister(X, Y) :-
      sibling(X, Y),
      female(X).

  brother_and_sister(X, Y) :-
      sibling(X, Y),
      male(X),
      female(Y).