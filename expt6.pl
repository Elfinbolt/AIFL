% Facts
items(kitchen,    [stove, counter, sink]).
items(dining,     [dining_table, chairs]).
items(bedroom1,   [bed, wardrobe, lamp]).
items(living,     [sofa, couch, coffee_table]).
items(bedroom2,   [bed, cupboard]).
items(study,      [desk, chair]).
items(diningnook, [round_table, chairs]).

connected(kitchen, dining).    connected(dining, kitchen).
connected(kitchen, bedroom1).  connected(bedroom1, kitchen).
connected(bedroom1, living).   connected(living, bedroom1).
connected(living, dining).     connected(dining, living).
connected(living, bedroom2).   connected(bedroom2, living).
connected(bedroom2, study).    connected(study, bedroom2).
connected(study, diningnook).  connected(diningnook, study).

% Display
show_items(Room) :-
    items(Room, I),
    write('Items in '), write(Room), write(': '), write(I), nl.

show_connected(Room) :-
    write('Connected rooms & their items:'), nl,
    connected(Room, R), show_items(R), fail.
show_connected(_).

% Start
start :-
    write('Rooms: kitchen, dining, bedroom1, living, bedroom2, study, diningnook'), nl,
    write('Enter room: '), read(Room), nl,
    (items(Room, _) ->
        show_items(Room), nl, show_connected(Room)
    ;
        write('Invalid room!')
    ).