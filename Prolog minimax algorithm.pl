% Define players
player(x).
player(o).

% Define the initial empty board
initial_board([e, e, e,
               e, e, e,
               e, e, e]).

% Winning positions
winning([P,P,P,_,_,_,_,_,_], P).
winning([_,_,_,P,P,P,_,_,_], P).
winning([_,_,_,_,_,_,P,P,P], P).
winning([P,_,_,P,_,_,P,_,_], P).
winning([_,P,_,_,P,_,_,P,_], P).
winning([_,_,P,_,_,P,_,_,P], P).
winning([P,_,_,_,P,_,_,_,P], P).
winning([_,_,P,_,P,_,P,_,_], P).

% Check for a draw
draw(Board) :- \+ member(e, Board), \+ winning(Board, x), \+ winning(Board, o).

% Check game over
game_over(Board, Winner) :- winning(Board, Winner), Winner \= e.
game_over(Board, draw) :- draw(Board).

% Replace element at index
replace([_|T], 0, X, [X|T]).
replace([H|T], I, X, [H|R]) :-
    I > 0, I1 is I - 1,
    replace(T, I1, X, R).

% Find all available moves
available_moves(Board, Moves) :-
    findall(I, (nth0(I, Board, e)), Moves).

% Minimax algorithm
minimax(Board, Player, BestMove, BestVal) :-
    game_over(Board, Winner), !,
    value(Winner, BestVal),
    BestMove = none.

minimax(Board, Player, BestMove, BestVal) :-
    available_moves(Board, Moves),
    findall(Val-Mv,
        (
            member(Mv, Moves),
            replace(Board, Mv, Player, NewBoard),
            switch_player(Player, Opponent),
            minimax(NewBoard, Opponent, _, Val1),
            invert(Val1, Val)
        ),
        Results),
    max_member(BestVal-BestMove, Results).

% Assign values to terminal states
value(x, 1).
value(o, -1).
value(draw, 0).

% Switch player
switch_player(x, o).
switch_player(o, x).

% Invert score for opponent
invert(1, -1).
invert(-1, 1).
invert(0, 0).
