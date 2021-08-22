# music-application

This application is for listening to your favorite songs and creating personalized
playlists.

## Database schema

- User table

  1. user_id: int, primary key, auto-increment
  2. username: varchar(50) not null, unique
  3. password: varchar(25) not null
  4. date_of_joining: timestamp not null
  5. last_login: timestamp

- Artist table

  1. artist_id: int, primary key, auto-increment
  2. name: varchar(50) not null

- Song table

  1. song_id: int, primary key, auto-increment
  2. name: varchar(50) not null
  3. artist_id: foreign key to Artists table
  4. url: varchar(200)

- SongLike table

  1. song_like_id: int, primary key, auto-increment
  2. song_id: foreign key to Songs table
  3. user_id: foreign key to Users table
  4. Unique constraint between song_id and user_id
