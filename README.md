# flask-blogly
 
 # create table users (id serial primary key, first_name varchar(50), last_name varchar(50), image_url text);
 # create table posts (id serial primary key, title text not null, content text, created_at timestamp, user_id integer references users on delete cascade);