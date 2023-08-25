greetings = input("Greeting: ").lower().strip()

if "hello" in greetings:
    print("$0")
elif greetings[0][0] == "h":
    print("$20")
else:
    print("$100")