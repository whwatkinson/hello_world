#!/usr/bin/env sh

echo '{"message": "Hello, World!"}' | jq -r '.message'
