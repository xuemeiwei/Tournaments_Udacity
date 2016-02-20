# Project 2: Tournaments_Udacity
<br>
This project uses PostgreSQL database to keep track of players and matches in a game tournament. The game tournament uses the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

This project has two parts: <br>
  1. Define the database schema (SQL table definitions);
  2. Write codes that will operate the database.

This project contains three files:

  1. tournament.sql: The definition of the database schema;
  2. tournament.py: Implementations of the functions;
  3. tournament_test.py: Unit tests that will test the functions in tournament.py.
  
How to run:
  1. Import the database scheme into PostgreSQL database using vagrant:

  Type: psql -> create database tournament -> \c tournament -> \i tournament.sql -> \q

  2. Run the test of this project by typing "python tournament_test.py":

  It will show the following information of successful running:

    1. Old matches can be deleted.
    2. Player records can be deleted.
    3. After deleting, countPlayers() returns zero.
    4. After registering a player, countPlayers() returns 1.
    5. Players can be registered and deleted.
    6. Newly registered players appear in the standings with no matches.
    7. After a match, players have updated standings.
    8. After one match, players with one win are paired.
    Success!  All tests pass!