# import time
# import pyautogui
# from pynput.keyboard import Controller
# from googletrans import Translator

# Keyboard = Controller()

# def translate_text(text, dest_languages):
#     translator = Translator()
#     translations = {}
#     for lang_code, lang_name in dest_languages.items():
#         try:
#             translation = translator.translate(text, dest=lang_code).text
#             translations[lang_name] = translation
#         except ValueError as e:
#             print(f"Error translating to {lang_name} ({lang_code}): {e}")
#     return translations

# def main():
#     text = input("Enter the text to translate: ")
#     dest_languages = {
#         'hi': 'Hindi',
#         'bn': 'Bengali',
#         'te': 'Telugu',
#         'mr': 'Marathi',
#         'ta': 'Tamil',
#         'ur': 'Urdu',
#         'gu': 'Gujarati',
#         'kn': 'Kannada',
#         'or': 'Odia',
#         'ml': 'Malayalam',
#         'pa': 'Punjabi',
#         # 'as': 'Assamese',
#         # 'mai': 'Maithili',
#         # 'sat': 'Santali',
#         # 'ks': 'Kashmiri',
#         'ne': 'Nepali',
#         'en': 'English',
#         'es': 'Spanish',
#         'ar': 'Arabic',
#         'fr': 'French',
#         'ru': 'Russian',
#         'zh-CN': 'Chinese',
#         'pt': 'Portuguese',
#         'de': 'German',
#         'ja': 'Japanese',
#         'ko': 'Korean',
#         'it': 'Italian',
#         'nl': 'Dutch',
#         'tr': 'Turkish',
#         'th': 'Thai',
#         'vi': 'Vietnamese',
#         'sv': 'Swedish',
#         'pl': 'Polish',
#         'id': 'Indonesian',
#         'el': 'Greek',
#         'cs': 'Czech',
#         'hu': 'Hungarian',
#         'fi': 'Finnish',
#         'no': 'Norwegian',
#         'da': 'Danish',
#         'sk': 'Slovak',
#         'ro': 'Romanian'
#     }
#     translations = translate_text(text, dest_languages)
#     for lang_name, translation in translations.items():
#         Keyboard.type(f"{lang_name}: {translation}")
#         time.sleep(1)
#         pyautogui.press("enter")
#         # if lang_name == "Nepali":
#         #     Keyboard.type("or chahiye kya")
#         #     pyautogui.press("enter")
#         #     Keyboard.type("or lo")
#         #     time.sleep(10)
#         #     pyautogui.press("enter")

# if __name__ == "__main__":
#     main()



from pytube import YouTube

url = "https://www.youtube.com/watch?v=75Y1y2fQFoc"
YouTube(url).streams.get_highest_resolution().download()
print("Download completed!")
