-- Creates Postgres table in DEV
create table if not exists AccessMonitor
(
created timestamp,
apiaddress text,
returncode int,
keywords text,
responsetime float,
PRIMARY KEY (created,apiaddress)
);
