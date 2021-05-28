DROP TABLE IF EXISTS teams
DROP TABLE IF EXISTS stadiums
DROP TABLE IF EXISTS players
DROP TABLE IF EXISTS leagues
DROP TABLE IF EXISTS associations
DROP TABLE IF EXISTS teams_players
DROP TABLE IF EXISTS leagues_teams



CREATE TABLE players(
    id SERIAL PRIMARY KEY,
    surname VARCHAR(255),
    first_name VARCHAR(255),
    squad_number INT, 
    position INT, -- RELATES ENUM VALUE
    goals INT,
    assists INT,
    own_goals INT,
    yellow_cards INT,
    red_cards INT,
    clean_sheets INT
);


--TEAMS: many to many with players (i.e. domestic and international)
CREATE TABLE teams(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    year_founded INT,
    stadium_id INT REFERENCES stadiums(id)

);

CREATE TABLE teams_players(
    id SERIAL PRIMARY KEY,
    teams_id INT REFERENCES teams(id),
    players_id INT REFERENCES players(id)
);

-- STADIUMS: one to many with teams (i.e. Milan/Inter)
CREATE TABLE stadiums(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    capacity INT
);

--Associations: one to many with leagues
CREATE TABLE associations(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

--Leagues: many to many with teams (i.e. domestic and european etc.)
CREATE TABLE leagues(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    association_id INT REFERENCES associations(id)
);

CREATE TABLE leagues_teams(
    id SERIAL PRIMARY KEY,
    league_id INT REFERENCES leagues(id),
    teams_id INT REFERENCES teams(id)
):

