#!/usr/bin/env bash

cat hello_world.sol_json.ast | jq -r '.nodes[1].nodes[0].body.statements[0].expression.value'
