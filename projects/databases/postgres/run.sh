#!/usr/bin/env bash

service postgresql start
su - postgres -c "psql -c \"SELECT 'Hello, World\!';\"" | tail -3 | head -1 | sed 's/\\//g' > output.txt
