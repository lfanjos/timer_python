import time


def main():
    seconds = get_input()

    counter(seconds)


def get_input():
    ipt = input("Insitra quantos segundos o timer deve contar: ")
    while not ipt.isnumeric() or int(ipt) // 2 == 0:
        ipt = input("Por favor, insira um valor válido: ")

    return int(ipt)


def counter(seconds):
    now = time.time()
    t_end = now + seconds

    while time.time() < t_end:
        print(seconds)
        seconds -= 1
        time.sleep(1)


if __name__ == "__main__":
    main()
