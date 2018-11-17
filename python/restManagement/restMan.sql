create table dbo.t_customer(
customer_id SERIAL PRIMARY KEY,
first_name text not null,
middle_name text,
last_name text not null
)


create table dbo.t_address (
address_id integer not null,
street_address_1 text,
street_address_2 text,
city character varying(255) not null,
state character(2),
zip_code character varying(10)
)

