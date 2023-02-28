import sys

def main():
    args = sys.argv[1:]
    if len(args) < 2:
        print("Ingrese al menos dos parámetros")
        exit(1)
    print(f'{args[0]} {args[1]}')

if __name__ == "__main__":
    main()
