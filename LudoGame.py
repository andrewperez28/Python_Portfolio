# Author: Andrew Perez
# GitHub username: andrewperez28
# Date: 7-26-22
# Description: A program that runs a simplified version of the board game Ludo. Up to 4 players can play and each player
#              has two tokens. In order for a player to win, both of the player's tokens must reach the finishing square
#              on an exact roll. The finishing square is approached via a player's home squares, which opponents cannot
#              enter. Tokens must exit their home yard, traverse around the board across 50 squares, traverse through
#              their respective home squares, and land on the finishing square in an exact roll. Tokens exit their home
#              yard upon rolling a 6. If a player rolls another Players can kick off opponent tokens if their token
#              lands on the same square, which will send the opponent's token back to their home yard. If a player lands
#              on their other own token, the two tokens are "stacked" and act as one, unless an opponent lands on that
#              stacked token. The stacked token would then be kicked off and separate back into two tokens upon
#              returning to the home yard.


class GameBoard:
    """An object representing the game board of the game. Used as composition for Player and LudoGame class and is
    required for many methods in the Player and LudoGame classes. Deals with Player paths, home squares, and bases.
    Automatically initialized by Player and LudoGame classes. Contains important methods used to get the square name of
    any squares tuple."""

    def __init__(self):
        """Initializes 4 data members, a_squares, b_squares, c_squares, d_squares. Each squares data member is a tuple
        representing the path of each of the player's positions. Each tuple starts with R and ends in E, but the rest
        of the elements vary according to the path. A's path goes from space R, spaces 1-50, spaces A1-A6, and then
        space E. B, C, and D loop around the 56th space. B's path goes from space R, spaces 15-8, spaces B1-B6, and then
         space E. C's path goes from space R, spaces 29-22, spaces C1-C6, and then space E. D's path goes from space R,
         spaces 43-36, spaces D1-D6, and then space E. They are tuples because elements will never be modified."""

        self._a_squares = ("R", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16",
                           "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31",
                           "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46",
                           "47", "48", "49", "50", "A1", "A2", "A3", "A4", "A5", "A6", "E")
        # Player A's squares, self-explanatory for next 3. Tuples because elements will never change

        self._b_squares = ("R", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28",
                           "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43",
                           "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "1", "2", "3",
                           "4", "5", "6", "7", "8", "B1", "B2", "B3", "B4", "B5", "B6", "E")

        self._c_squares = ("R", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42",
                           "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "1", "2",
                           "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18",
                           "19", "20", "21", "22", "C1", "C2", "C3", "C4", "C5", "C6", "E")

        self._d_squares = ("R", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "1",
                           "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18",
                           "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33",
                           "34", "35", "36", "D1", "D2", "D3", "D4", "D5", "D6", "E")

    def get_squares(self, player):
        """Returns the tuple of the squares of the indicated player. Argument must be either A, B, C, or D as a
        string"""
        if player == "A":
            return self._a_squares
        elif player == "B":
            return self._b_squares
        elif player == "C":
            return self._c_squares
        elif player == "D":
            return self._d_squares

    def get_square_name(self, what_square, shared_space_index):
        """Getter method that returns the string that is found in the provided index of square data member tuple. 1st
        argument must be one of the 4 square data members tuples(A, B, C, or D). 2nd argument must be an int and is a
        valid index for the specific square data member tuple."""
        return what_square[shared_space_index]


class Player:
    """A class representing a Player in the game. Uses GameBoard object via composition.  Holds information regarding
    token step count and player status. The information is very important for LudoGame class methods. Has the ability to
     get space name of each token from the use of GameBoard methods."""

    def __init__(self, board, player):
        """The initialization of the class contains 10 data members, depending on which of the 4 positions is chosen for
         the player. The first argument must be a GameBoard object, which requires access to the methods via
         composition. The second argument must be a string as either “A”, “B”, “C”, or “D”. These two arguments are also
          used as data members. The self._completed data member is initialized to False, it only changes to True if that
           player has both of their p and q tokens on E. The self._stacked data member is also initialized to False, and
            represents if the player’s tokens are stacked. The self._start_space and self._end_space are the start and
            end spaces of the corresponding player, depending on position. The data members self._p_token and
            self._q_token both are initialized to “H”, as that represents the home yard position. Both the self._p_steps
             and self._q_steps are initialized to -1, which also represents the home yard position. They represent the
             total number of steps for each token."""

        self._board = board  # Must be a GameBoard object
        self._player = player  # Position, is either "A", "B", "C", or "D"
        self._completed = False  # True if player has both tokens on "E" square
        self._stacked = False  # True if both p and q tokens are in one space together
        if player == "A":
            self._start_space = "1"
            self._end_space = "50"
            self._p_token = "H"
            self._q_token = "H"
            self._p_steps = -1  # -1 is home yard position
            self._q_steps = -1

        elif player == "B":
            self._start_space = "15"
            self._end_space = "8"
            self._p_token = "H"
            self._q_token = "H"
            self._p_steps = -1
            self._q_steps = -1

        elif player == "C":
            self._start_space = "29"
            self._end_space = "22"
            self._p_token = "H"
            self._q_token = "H"
            self._p_steps = -1
            self._q_steps = -1

        elif player == "D":
            self._start_space = "43"
            self._end_space = "36"
            self._p_token = "H"
            self._q_token = "H"
            self._p_steps = -1
            self._q_steps = -1

    def __repr__(self):
        """Makes the Player object become readable, returns a string"""
        return f"Player {self._player}"

    def get_player(self):
        """Getter method for self._player, returns a string"""
        return self._player

    def get_completed(self):
        """Getter method that returns True if Player has finished the game and returns False if Player has NOT finished
         the game."""
        return self._completed

    def set_completed(self):
        """Setter method for self._competed, only sets to True when Player has won."""
        self._completed = True

    def get_stacked(self):
        """Getter method that returns self._stacked as a bool, True or False."""
        return self._stacked

    def set_stacked(self, change):
        """Setter method that changes self._stacked to either True or False. 1st argument must either be the bool True
        or False"""
        self._stacked = change

    def get_start_space(self):
        """Getter method that returns self._start_space, returns a string"""
        return self._start_space

    def get_end_space(self):
        """Getter method that returns self._end_space, returns a string"""
        return self._end_space

    def get_p_token(self):
        """Getter method for self._p_token, returns a string"""
        return self._p_token

    def get_q_token(self):
        """Getter method for self._q_token, returns a string"""
        return self._q_token

    def get_token_p_step_count(self):
        """Getter method that returns the total steps of the Player's 'p' token as an int"""
        return self._p_steps

    def set_token_p_step_count(self, steps):
        """Setter method for self._p_steps"""
        self._p_steps = steps

    def get_token_q_step_count(self):
        """Getter method that returns the total steps of the Player's 'q' token"""
        return self._q_steps

    def set_token_q_step_count(self, steps):
        """Setter method for self._q_steps"""
        self._q_steps = steps

    def get_space_name(self, total_steps_of_token):
        """Returns the name of the space the token has landed on based on the total number of steps presented as a
        string. 1st argument must use self.get_token_p/q_step_count"""
        if total_steps_of_token == -1:  # Is home yard position
            return "H"
        return self._board.get_square_name(self._board.get_squares(self._player), total_steps_of_token)

    def set_p_token(self):
        """Setter method for self._p_token"""
        self._p_token = self.get_space_name(self._p_steps)

    def set_q_token(self):
        """Setter method for self._q_token"""
        self._q_token = self.get_space_name(self._q_steps)


class LudoGame:
    """This class represents the actual play of the game. Player and BoardGame objects are initialized using this class.
     The class’s responsibilities are holding the actual Player objects, initializing the BoardGame class, moving the
     tokens, and deciding upon which token will be moved according to the current turn of the game. Uses many Player
     and BoardGame methods"""

    def __init__(self):
        """The initialization of the class contains 2 data members. The data member self._board initializes a GameBoard
        class and is used via composition. The data member self._player_objects is initialized as an empty dictionary,
        where the keys will be the player’s positions represented as a string “A”, “B”, “C” or “D” and the values will
        be the corresponding Player objects. This empty dictionary will be filled upon the calling of
        player_initialization()."""

        self._board = GameBoard()  # Needs access to methods via composition
        self._player_objects = {}  # "A", "B", "C", or "D" is key, associating player object is value

    def get_board(self):
        """Getter method for self._board, returns an object."""
        return self._board

    def get_player_objects(self):
        """Getter method for self._player_objects, returns a dictionary"""
        return self._player_objects

    def set_player_objects(self, player_object):
        """Setter method for self._player_objects, uses the list of players given"""
        self._player_objects[player_object.get_player()] = player_object

    def get_player_by_position(self, player_position):  # Arg represented as a string
        """Returns the player object occupying the player_position(string), if given an invalid string parameter, will
        return 'Player not found!'"""
        if player_position in self._player_objects:
            return self._player_objects[player_position]
        return "Player not found!"

    def move_token(self, player_object, token_name, token_steps):
        """Method that moves a player’s token. The first argument must be a Player object. The 2nd argument must be the
        name of a token as a string, either “p” or “q”. The 3rd argument must be an int and the int must be between 1
        and 6. This method calls upon many methods from the GameBoard and Player classes. Does not return anything and
        is closely related to the algorithm() method."""

        if token_name == "p":
            if player_object.get_token_p_step_count() + token_steps > 57:  # Bounce back, no win
                target_space_index = 57 - ((player_object.get_token_p_step_count() + token_steps) - 57)
                #  Adjusted target_space_index to prevent going over 57
            else:
                target_space_index = player_object.get_token_p_step_count() + token_steps  # Normal target_space_index

        elif token_name == "q":
            if player_object.get_token_q_step_count() + token_steps > 57:
                target_space_index = 57 - ((player_object.get_token_p_step_count() + token_steps) - 57)
            else:
                target_space_index = player_object.get_token_q_step_count() + token_steps

        target_space_name = self._board.get_square_name(self._board.get_squares(player_object.get_player()),
                                                        target_space_index)  # Looking ahead at what landing space is
        opponent = None  # Stays at None if there's no opponent occupying target_space_name
        for each_opponent in self._player_objects.values():
            if each_opponent != player_object:
                opponent_p = each_opponent.get_p_token()
                opponent_q = each_opponent.get_q_token()
                if opponent_p == target_space_name:  # Opponent's p token is found on target_space_name
                    opponent = each_opponent
                elif opponent_q == target_space_name:  # Opponent's q token is found on target_space_name
                    opponent = each_opponent

        if opponent is not None:
            if opponent.get_stacked() is True and opponent_p != "E" and opponent_q != "E":
                # Kick opponent's stacked tokens
                opponent.set_stacked(False)  # Opponent is no longer stacked
                opponent.set_token_p_step_count(-1)  # p step count is now -1
                opponent.set_token_q_step_count(-1)  # q step count is now -1
                opponent.set_p_token()  # p space is now H
                opponent.set_q_token()  # q space is now H

            elif opponent_p == target_space_name and opponent_p != "E":
                # It's opponent's p token on landing space, kick
                opponent.set_token_p_step_count(-1)
                opponent.set_p_token()

            elif opponent_q == target_space_name and opponent_q != "E":
                # It's opponent's q token on landing space, kick
                opponent.set_token_q_step_count(-1)
                opponent.set_q_token()

        if player_object.get_stacked() is True:  # Move both the player's p and q token at the same time
            player_object.set_token_p_step_count(target_space_index)  # Update step count
            player_object.set_p_token()  # Update token space name
            player_object.set_token_q_step_count(target_space_index)
            player_object.set_q_token()
        else:
            if token_name == "p":  # Move only player's p token
                player_object.set_token_p_step_count(target_space_index)
                player_object.set_p_token()
            elif token_name == "q":  # Move only player's q token
                player_object.set_token_q_step_count(target_space_index)
                player_object.set_q_token()
        if player_object.get_p_token() == player_object.get_q_token() and player_object.get_p_token() != "R":
            # If player's other token is on same space but not the ready to go position
            player_object.set_stacked(True)  # Player is now stacked

    def algorithm(self, player_object, roll):
        """Method that returns a string, either “p” or “q”. Determines whether the player’s p token or q token will
         move. First, it checks whether the q token has left the home yard. If not, then p is chosen. Second, it checks
         whether any of the tokens are on the finishing square, E. If p is on E, q is chosen and vice versa. Third, it
         checks whether any of the tokens are in the kicking position. If both p and q are in kicking positions, then
         the token furthest from the finishing square is chosen. If no tokens are in kicking positions, then the token
         from furthest from the finishing square is chosen. """

        p_token_steps = player_object.get_token_p_step_count()
        q_token_steps = player_object.get_token_q_step_count()
        # First, check if q token has left home yard, if not, then automatically choose p
        if player_object.get_q_token() == "H":  # q token is still at home yard, automatically choose p
            return "p"

        # Second, check if any of the tokens are already finished on E
        if p_token_steps == 57:  # p is finished
            return "q"

        if q_token_steps == 57:  # q is finished
            return "p"

        # Third, check if any tokens are in position to go to winning square
        else:
            p_landing_index = p_token_steps + roll
            q_landing_index = q_token_steps + roll

            if p_landing_index > 57:
                p_landing_index = 57 - ((player_object.get_token_p_step_count() + roll) - 57)
                #  Adjusted landing_index to prevent going over 57, same for q

            if q_landing_index > 57:
                q_landing_index = 57 - ((player_object.get_token_q_step_count() + roll) - 57)

            p_landing_space = self._board.get_square_name(self._board.get_squares(player_object.get_player()),
                                                          p_landing_index)
            q_landing_space = self._board.get_square_name(self._board.get_squares(player_object.get_player()),
                                                          q_landing_index)
            if p_landing_index == 57:  # p can finish
                return "p"

            elif q_landing_index == 57:  # q can finish
                return "q"
            # Fourth, check if any tokens are in position to kick an opponent's token
            else:
                p_can_kick = False  # Changes to True if token can kick
                q_can_kick = False
                opponent_kick_list = []  # A list of player_object's opponent's spaces used to check for kicking

                for each_opponent in self._player_objects.values():
                    if each_opponent is player_object:  # Makes sure player_object isn't an opponent
                        pass
                    else:
                        opponent_kick_list.append(each_opponent.get_p_token())  # Append opponent's p token space
                        opponent_kick_list.append(each_opponent.get_q_token())  # Append opponent's q token space

                if p_landing_space in opponent_kick_list:  # p can kick
                    p_can_kick = True

                if q_landing_space in opponent_kick_list:  # q can kick
                    q_can_kick = True

                if p_can_kick is True and q_can_kick is True:  # Check which token is furthest from finishing square
                    if q_token_steps < p_token_steps:
                        return "q"  # q is furthest from finishing square
                    else:
                        return "p"  # p is furthest from finishing square

                elif p_can_kick is True:
                    return "p"

                elif q_can_kick is True:
                    return "q"

                # Finally, check with tokens are furthest from finishing square
                else:
                    if q_token_steps < p_token_steps:
                        return "q"  # q is furthest from finishing square

                    else:
                        return "p"  # p is furthest from finishing square

    def player_initialization(self, player_list):
        """Initializes Player objects from the player_list argument. Is only used by play_game. Argument must be a list
        of players represented as a string. The strings can only be 'A', 'B', 'C', or 'D'."""
        for each_player in player_list:
            if each_player == "A":
                player_a = Player(self._board, each_player)
                self.set_player_objects(player_a)

            elif each_player == "B":
                player_b = Player(self._board, each_player)
                self.set_player_objects(player_b)

            elif each_player == "C":
                player_c = Player(self._board, each_player)
                self.set_player_objects(player_c)

            elif each_player == "D":
                player_d = Player(self._board, each_player)
                self.set_player_objects(player_d)

            else:
                return "Invalid player in the list! Must be either 'A', 'B', 'C', or 'D'"

    def play_game(self, player_list, turns_list):  # Arg 1 is the list of players, arg 2 is the list of turns
        """Creates Player objects based on player_list passed in. Player list must be a list of strings where the
         strings must be either "A", "B", "C", or "D". These strings will be used to make the corresponding Player
         objects. Turns list must be a list of  size 2 tuples. The 0 index of the tuple must be either "A", "B", "C", or
          "D" and the 1 index of the tuple must be an int between 1 and 6. Method will then return a list of strings
          representing the current spaces of all the tokens for each Player after all turns have passed based on
          turns_list. Order is p token followed by q token of a Player object in alphabetical order."""

        self.player_initialization(player_list)  # Initialize all necessary players based on player_list
        end_of_round_turn_list = []  # Will populate with each player's p/q tokens in that order
        for each_turn in turns_list:  # Parsing turns_list
            current_player = self._player_objects[each_turn[0]]
            player_roll = each_turn[1]
            if current_player.get_completed() is True:  # Do nothing this turn as current_player is already finished
                pass
            else:

                if player_roll == 6 and current_player.get_p_token() == "H":  # p exits home yard and goes to ready
                    current_player.set_token_p_step_count(0)
                    current_player.set_p_token()

                elif player_roll == 6 and current_player.get_q_token() == "H":  # q exits home yard and goes to ready
                    current_player.set_token_q_step_count(0)
                    current_player.set_q_token()

                elif current_player.get_p_token() == "H" and current_player.get_q_token() == "H":  # No 6, no home exits
                    pass

                else:
                    decision = self.algorithm(current_player, player_roll)  # Decide if token p or token q is chosen
                    self.move_token(current_player, decision, player_roll)  # Move token

            if current_player.get_p_token() == "E" and current_player.get_q_token() == "E":  # current_player finished
                current_player.set_completed()

        for each_player in self._player_objects.values():  # Build end_of_round_list
            end_of_round_turn_list.append(each_player.get_p_token())
            end_of_round_turn_list.append(each_player.get_q_token())
        return end_of_round_turn_list
