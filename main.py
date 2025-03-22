from cli.commands import process_command

def main():
    while True:
        try:
            cmd = input("# ").strip()
            if cmd.upper() == "EXIT":
                break
            print(process_command(cmd))

        except Exception as e:
            print(f"Error - {e}")

if __name__ == "__main__":
    main()
