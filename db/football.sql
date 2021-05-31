DROP TABLE IF EXISTS signings;
DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS stadiums;
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS fixtures;
DROP TABLE IF EXISTS seasons;
DROP TABLE IF EXISTS leagues;
DROP TABLE IF EXISTS associations;
DROP TABLE IF EXISTS participants;


CREATE TYPE pos AS ENUM ('GK', 'DEF', 'MID', 'FWD');

CREATE TABLE players(
    id SERIAL PRIMARY KEY,
    surname VARCHAR(255),
    first_name VARCHAR(255),
    squad_number INT, 
    --position INT, -- RELATES ENUM VALUE
    position pos,
    goals INT,
    assists INT,
    own_goals INT,
    yellow_cards INT,
    red_cards INT,
    clean_sheets INT
);

-- STADIUMS: one to many with teams (i.e. Milan/Inter)
CREATE TABLE stadiums(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255),
    capacity INT
);


--TEAMS: many to many with players (i.e. domestic and international)
CREATE TABLE teams(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    year_founded INT,
    stadium_id INT REFERENCES stadiums(id)
);

CREATE TABLE signings(
    id SERIAL PRIMARY KEY,
    team_id INT REFERENCES teams(id),
    player_id INT REFERENCES players(id),
    signed_on DATE
);

--Associations: one to many with leagues
CREATE TABLE associations(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

--Leagues: many to many with teams (i.e. domestic and european etc.)
--Leagues: one to many with seasons
CREATE TABLE leagues(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    association_id INT REFERENCES associations(id)
);

--Seasosn: one to many with fixtures
CREATE TABLE seasons(
    id SERIAL PRIMARY KEY,
    year VARCHAR(255),
    league_id INT REFERENCES leagues(id)
);



CREATE TABLE fixtures(
    id SERIAL PRIMARY KEY,
    home_id INT REFERENCES teams(id),
    away_id INT REFERENCES teams(id),
    season_id INT REFERENCES seasons(id),
    home_score INT,
    away_score INT
);

CREATE TABLE participants(
    id SERIAL PRIMARY KEY,
    league_id INT REFERENCES leagues(id),
    team_id INT REFERENCES teams(id)
);
