# music-application

This application is for listening to your favourite songs and creating personalised playlists.

## Database schema

- Users table
  1. user_id: int, primary key, autoincrement
  2. username: varchar(50) not null, unique
  3. password: varchar(25) not null
  4. date_of_joining: timestamp not null
  5. last_login: timestamp

- Artists table
  1. artist_id: int, primary key, autoincrement
  2. name: varchar(50) not null

- Songs table
  1. song_id: int, primary key, autoincrement
  2. name: varchar(50) not null
  3. artist_id: foreign key to Artists table
  4. url: varchar(200) 

- Song_likes table
  1. song_id: foreign key to Songs table
  2. user_id: foreign key to Users table
  3. Unique constraint between song_id and user_id

