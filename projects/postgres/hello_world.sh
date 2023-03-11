#!/usr/bin/env bash



postgres && echo "SELECT 'Hello, World\!' AS hello_message;" | psql 'postgresql://postgres:postgres@localhost:5432/postgres'
