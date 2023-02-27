#!/bin/bash

/docker-entrypoint.sh neo4j
sleep 15
echo "MATCH (Hello:Word) RETURN 'Hello, World\!';" | cypher-shell --fail-fast -a "neo4j://localhost:7687" -u "neo4j" -p "wiggle"

