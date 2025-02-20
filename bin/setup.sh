#!/bin/bash

URL="http://localhost:8080"
ROOM="m2"

# Tutor
xdg-open "${URL}/${ROOM}/tutor" &
sleep 0.5  # Optional delay

# Poll
xdg-open "${URL}/${ROOM}/poll" &
sleep 0.5  # Optional delay

# Learner
for i in {1..2}; do
    xdg-open "${URL}/${ROOM}" &
    sleep 0.5  # Optional delay
done

