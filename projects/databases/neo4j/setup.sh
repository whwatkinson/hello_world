#!/usr/bin/env bash

echo 'dbms.security.auth_enabled: false' >> /var/lib/neo4j/conf/neo4j.conf

neo4j start

cat hello_world.cypher | cypher-shell > output.txt
