-- 最初にデータベースを作成するSQL
create database app_db_development;
create database app_db_test;
grant all privileges on database app_db_development to deploy;
grant all privileges on database app_db_test to deploy;
