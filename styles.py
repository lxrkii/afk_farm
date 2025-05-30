# Цветовая палитра для теплых зеленых тонов
# Используем более мягкие и глубокие зеленые оттенки
GREEN_PRIMARY_DARK = "#3D6F42"   # Глубокий зеленый для кнопок
GREEN_PRIMARY_LIGHT = "#5A9460"  # Светлый акцент на кнопках (для hover)
GREEN_ACCENT = "#8BC34A"         # Яркий зеленый для контраста (например, для текста выхода)
BACKGROUND_DARK = "#2E3A32"      # Очень темный, почти черный зеленый для основного фона (имитация "блюра")
BACKGROUND_LIGHT = "#404F43"     # Чуть светлее для фреймов или подложек
TEXT_LIGHT = "#E8EAE6"           # Светлый текст
TEXT_DARK = "#2C2C2C"            # Темный текст для полей ввода

# Основные стили
MAIN_BG = BACKGROUND_DARK
BUTTON_BG = GREEN_PRIMARY_DARK
BUTTON_ACTIVE_BG = GREEN_PRIMARY_LIGHT # Цвет при наведении на кнопку
BUTTON_FG = TEXT_LIGHT
BUTTON_ACTIVE_FG = TEXT_LIGHT
LABEL_FG = TEXT_LIGHT
ENTRY_BG = TEXT_LIGHT
ENTRY_FG = TEXT_DARK

FONT_FAMILY = "Segoe UI" # Или "Roboto", "Open Sans" - если доступны
FONT_SIZE = 11
FONT_WEIGHT = "bold"

# Стиль кнопок
button_style = {
    "font": (FONT_FAMILY, FONT_SIZE, FONT_WEIGHT),
    "bg": BUTTON_BG,
    "fg": BUTTON_FG,
    "activebackground": BUTTON_ACTIVE_BG,
    "activeforeground": BUTTON_ACTIVE_FG,
    "bd": 2,
    "relief": "ridge",
    "padx": 25,
    "pady": 12,
    "width": 10
}

cooking_button_style = {
    "font": (FONT_FAMILY, FONT_SIZE, FONT_WEIGHT),
    "bg": BUTTON_BG,
    "fg": BUTTON_FG,
    "activebackground": BUTTON_ACTIVE_BG,
    "activeforeground": BUTTON_ACTIVE_FG,
    "bd": 2,
    "relief": "ridge",
    "padx": 25,
    "pady": 12,
    "width": 2
}

# Стиль кнопки выхода
exit_button_style = {
    "font": (FONT_FAMILY, FONT_SIZE, FONT_WEIGHT),
    "bg": MAIN_BG,
    "fg": GREEN_ACCENT,
    "activebackground": BACKGROUND_LIGHT,
    "activeforeground": GREEN_ACCENT,
    "bd": 0,
    "padx": 20,
    "pady": 10,
    "relief": "flat",
    "width": 15
}

# Стиль кнопки помощи (исправлены отрицательные отступы)
git_button = {
    "font": (FONT_FAMILY, FONT_SIZE, FONT_WEIGHT),
    "bg": BACKGROUND_LIGHT, 
    "fg": TEXT_LIGHT,
    "activebackground": GREEN_PRIMARY_DARK,
    "activeforeground": TEXT_LIGHT,
    "bd": 1,
    "relief": "flat",
    "padx": 10, # Изменено с -10 на 10
    "pady": 5,  # Изменено с -10 на 5 (или любое другое положительное значение)
    "width": 15
}

# Стиль меток
label_style = {
    "font": (FONT_FAMILY, FONT_SIZE, FONT_WEIGHT),
    "fg": LABEL_FG,
    "bg": MAIN_BG
}

# Стиль полей ввода
entry_style = {
    "font": ("Arial", FONT_SIZE, "normal"),
    "bg": ENTRY_BG,
    "fg": ENTRY_FG,
    "relief": "solid",
    "bd": 1,
    "highlightbackground": GREEN_PRIMARY_DARK,
    "highlightthickness": 1
}