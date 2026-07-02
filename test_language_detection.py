from settings import Settings
import os

print("=" * 60)
print("Testing Language Detection")
print("=" * 60)
print()

if os.path.exists("config.json"):
    os.remove("config.json")
    print("Removed existing config.json")
    print()

settings = Settings()
detected_lang = settings.get("ui_language")

print(f"Detected system language: {detected_lang}")
print()

if detected_lang == "russian":
    print("✓ Russian system detected - UI will be in Russian")
else:
    print("✓ English/Other system detected - UI will be in English")

print()
print("You can change the language in Settings within the app.")
print("=" * 60)
