#!/bin/bash
# Считаем обновления
count=$(checkupdates | wc -l)

# Выводим строго JSON
if [ "$count" -gt 0 ]; then
    echo "{\"text\": \"$count\", \"class\": \"pending\"}"
else
    echo "{\"text\": \"0\", \"class\": \"updated\"}"
fi
