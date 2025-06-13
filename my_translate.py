import argostranslate.package
import argostranslate.translate

def translate_text(text, from_lang="en", to_lang="hi"):
    """
    Translate text using Argos Translate

    Args:
        text (str): Text to translate
        from_lang (str): Source language code (default: "en")
        to_lang (str): Target language code (default: "hi")

    Returns:
        str: Translated text
    """
    # Download language packs (e.g., English to Hindi)
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    package = next(filter(lambda x: x.from_code == from_lang and x.to_code == to_lang, available_packages))
    argostranslate.package.install_from_path(package.download())
    
    translated_text = argostranslate.translate.translate(text, from_lang, to_lang)
    # hindi_translation = argostranslate.translate.translate(text, "en", "hi")


    return translated_text