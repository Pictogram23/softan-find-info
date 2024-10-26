create table users (
    id serial not null unique,
    name text not null default '',
    email text not null default '',
    token text not null default '',
    refresh_token text not null default '',
    google_uid text not null default '',
    created_at timestamp with time zone default current_timestamp,
    updated_at timestamp with time zone default current_timestamp,
    constraint user_pkey primary key(id)
);
