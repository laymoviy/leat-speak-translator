import json
import os
import locale
import sys

class Settings:
    def __init__(self):
        self.config_file = "config.json"
        self.settings = self.load_settings()
    
    def get_system_language(self):
        try:
            if sys.platform.startswith('win'):
                import ctypes
                windll = ctypes.windll.kernel32
                lang_id = windll.GetUserDefaultUILanguage()
                if lang_id == 1049:
                    return "russian"
            else:
                system_locale = locale.getdefaultlocale()[0]
                if system_locale and system_locale.startswith('ru'):
                    return "russian"
        except:
            try:
                system_locale = locale.getdefaultlocale()[0]
                if system_locale and system_locale.startswith('ru'):
                    return "russian"
            except:
                pass
        
        return "english"
    
    def load_settings(self):
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                pass
        
        system_lang = self.get_system_language()
        return {
            "ui_language": system_lang
        }
    
    def save_settings(self):
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.settings, f, indent=4)
    
    def get(self, key):
        return self.settings.get(key)
    
    def set(self, key, value):
        self.settings[key] = value
        self.save_settings()
