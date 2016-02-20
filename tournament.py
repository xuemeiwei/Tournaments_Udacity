#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
    	return psycopg2.connect("dbname=tournament")
    except psycopg2.Error as e:
	print "Database connect failed”
      	exit()


def deleteMatches():
    """Remove all the match records from the database."""
    try:
    	DB = connect()
    	curs = DB.cursor()
    	curs.execute("delete from games;")
    	DB.commit()
    	DB.close()
    except psycopg2.Error as e:
	print "Database delete failed”
      	exit()
    


def deletePlayers():
    """Remove all the player records from the database."""
    try:
    	DB = connect()
    	curs = DB.cursor()
    	curs.execute("delete from players;")
    	DB.commit()
    	DB.close()
    except psycopg2.Error as e:
	print "Database delete failed”
      	exit()


def countPlayers():
    """Returns the number of players currently registered."""
    try:
    	DB = connect()
    	curs = DB.cursor()
    	curs.execute("select count(*) from players;")
    	num = curs.fetchone()
    	DB.close()
    	return num[0]
    except psycopg2.Error as e:
	print “count players failed”
      	exit()


def registerPlayer(name):/Users/xuemeiwei/Documents/udacity/fullstack-nanodegree-vm/vagrant/tournament/tournament.sql
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    try:
    	DB = connect()
    	curs = DB.cursor()
    	curs.execute("insert into players values (%s);",(name,))
    	DB.commit()
    	DB.close()
    except psycopg2.Error as e:
	print “Register players failed”
      	exit()



def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()
    curs = DB.cursor()
    curs.execute("select * from rankings;")
    standings = curs.fetchall()
    DB.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    curs = DB.cursor()
    curs.execute("insert into games values (%s,%s);",(winner, loser))
    DB.commit()
    DB.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    rankings = playerStandings()
    for i in range(1, len(rankings), 2):
	return [rankings[i-1][0], rankings[i-1][1], rankings[i][0], rankings[i][1]]
