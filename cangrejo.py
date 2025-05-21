import webbrowser

respuesta = input("eres un cangrejo? (si / no): ").strip()

if respuesta in ["si"]:
    webbrowser.open("https://www.youtube.com/watch?v=7gjv0kFSV94")
else:
    print("ª")
