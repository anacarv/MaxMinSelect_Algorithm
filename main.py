def max_min_select(arr, left, right):
    if left == right:
        return arr[left], arr[left]

    if right == left + 1:
        if arr[left] < arr[right]:
            return arr[left], arr[right]
        else:
            return arr[right], arr[left]

    mid = (left + right) // 2
    min1, max1 = max_min_select(arr, left, mid)
    min2, max2 = max_min_select(arr, mid + 1, right)

    return min(min1, min2), max(max1, max2)

def get_valid_input():
    while True:
        try:
            user_input = input("Digite uma lista de números inteiros separados por espaço: ").strip()
            if not user_input:
                raise ValueError("A lista não pode estar vazia.")
            arr = list(map(int, user_input.split()))
            return arr
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar apenas números inteiros separados por espaço.")

if __name__ == "__main__":
    arr = get_valid_input()
    print(f"Lista de entrada: {arr}")
    min_val, max_val = max_min_select(arr, 0, len(arr) - 1)
    print(f"Menor elemento: {min_val}, Maior elemento: {max_val}")
