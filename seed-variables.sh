#!/bin/bash

if [ ! -f .env ]; then
    cp .env.tpl /app/.env
    echo "Copied .env.tpl to /app/.env Please fill in the actual values in the .env file."
fi