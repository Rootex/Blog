create table if not exists users (
    id integer primary key autoincrement,
    username text not null,
    password text not null
);

create table if not exists posts (
    id integer primary key autoincrement,
    title text not null,
    post text not null,
    date text not null
);

insert into users (username, password) values ('admin', 'default');