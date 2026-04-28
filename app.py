from ai_engine import analyze_change_request

def main():
    print("=== Change Management Automation ===")

    description = input("Enter change request: ")

    result = analyze_change_request(description)

    print("\nAI Decision:")
    print(result)


if __name__ == "__main__":
    main()
