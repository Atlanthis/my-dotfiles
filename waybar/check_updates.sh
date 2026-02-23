#!/usr/bin/fish
# Проверка через paru (совмещает репозитории и AUR)
set updates (paru -Qu | wc -l)

if test "$updates" -gt 0
    # Отдаем JSON для Waybar: текст с числом и класс 'pending' для стиля
    echo "{\"text\": \"$updates\", \"class\": \"pending\"}"
else
    echo "{\"text\": \"0\", \"class\": \"up-to-date\"}"
end
