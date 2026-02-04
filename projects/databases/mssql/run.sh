#!/usr/bin/env bash

# Start SQL Server and hide the engine noise
/opt/mssql/bin/sqlservr > /dev/null 2>&1 &
SQL_PID=$!

SQLCMD="/opt/mssql-tools18/bin/sqlcmd"

# Wait for it to wake up
for i in {1..50}; do
    $SQLCMD -S localhost -U sa -P "$MSSQL_SA_PASSWORD" -C -Q "SELECT 1" > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        break
    fi
    sleep 1
done

# Run your query
$SQLCMD -S localhost -U sa -P "$MSSQL_SA_PASSWORD" -C \
    -Q "SET NOCOUNT ON; SELECT 'Hello, World!';" -W -h -1 > output.txt

# This is now the ONLY thing that will hit stdout
cat output.txt
