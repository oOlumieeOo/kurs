from datetime import datetime


def main():
    name = input("Атыңызды енгізіңіз: ").strip()
    today = datetime.now().strftime("%d.%m.%Y")
    print(f"Сәлем, {name}! Бүгін {today}")


if __name__ == "__main__":
    main()

