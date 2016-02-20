-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


drop view if exists rankings;
drop view if exists winners;
drop view if exists losers;
drop table if exists games;
drop table if exists players;

create table players(
	name text primary key,
	ID serial,
);

create table games(
	winnerID serial references players (ID),
	loserID serial references players (ID),
	matchID serial primary key,
);

create view losers as
select ID, count(loserID) as times
from players left join games
on players. ID = games.loserID
group by ID 
order by times desc;

create view winners as
select ID, count(winnerID) as times
from players left join games
on players.ID = games.winnerID
group by ID
order by times desc;


create view rankings as
select wins.ID as ID, name, winners.times as wins, winners.times+losers.times as matches 
from players, losers, winners
where players.ID = winners.ID and players.ID = losers.ID 
order by wins desc;
