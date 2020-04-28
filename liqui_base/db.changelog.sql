--liquibase formatted sql


--changeset dkmdebugin:1
create table testing (
    id int primary key,
    name varchar(50) not null
);

--changeset dkmdebugin:2
drop table testing;

