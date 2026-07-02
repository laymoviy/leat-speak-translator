class Translations:
    def __init__(self):
        self.translations = {
            "english": {
                "title": "Leet Speak Generator",
                "input_label": "Input Text",
                "output_label": "Leet Speak",
                "clear_button": "Clear",
                "copy_button": "Copy Leet Speak",
                "settings_button": "Settings",
                "settings_title": "Settings",
                "ui_language": "Interface Language:",
                "input_language": "Input Language:",
                "english": "English",
                "russian": "Russian",
                "close_button": "Close",
                "language_label": "Language:"
            },
            "russian": {
                "title": "Генератор Leet Speak",
                "input_label": "Исходный текст",
                "output_label": "Leet Speak",
                "clear_button": "Очистить",
                "copy_button": "Копировать Leet Speak",
                "settings_button": "Настройки",
                "settings_title": "Настройки",
                "ui_language": "Язык интерфейса:",
                "input_language": "Язык ввода:",
                "english": "Английский",
                "russian": "Русский",
                "close_button": "Закрыть",
                "language_label": "Язык:"
            }
        }
    
    def get(self, key, language):
        return self.translations.get(language, self.translations["english"]).get(key, key)
