#!/bin/bash

rm -f db/sqlite.db
sqlite3 db/sqlite.db < db/schema.sql
