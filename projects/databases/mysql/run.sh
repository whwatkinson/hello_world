#!/usr/bin/env bash

# Start MySQL service
service mysql start

# Run Hello World query and extract only the result
mysql -u root -e "SELECT 'Hello, World\!';" \
  | tail -n +2 > output.txt