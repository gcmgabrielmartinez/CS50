
def main():
    greetings = input("Greeting: ").strip()
    v = value(greetings)
    print(f"${v}")

def value(greeting):
    if "hello" in greeting.lower():
        return 0
    elif greeting[0][0].lower() == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()