pg_dump -n "public" --no-acl --no-owner --clean -h localhost tinyblog | heroku pg:psql --app tinyblog-dev
