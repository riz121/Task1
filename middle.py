def look_and_say_middle_two(n: int) -> str:
    if n < 1:
        raise ValueError("n must be a positive integer")

    term = "1"
    for _ in range(1, n):
        next_term = ""
        i = 0
        while i < len(term):
            count = 1
            while i + 1 < len(term) and term[i] == term[i + 1]:
                i += 1
                count += 1
            next_term += f"{count}{term[i]}"
            i += 1
        term = next_term

    mid_index = len(term) // 2
    # Return the middle two digits
    if len(term) % 2 == 0:
        return term[mid_index - 1:mid_index + 1]
    else:
        # Odd length, return the two middle digits (round down)
        return term[mid_index - 1:mid_index + 1]
        


if __name__ == "__main__":
    n = int(input("Enter n (4 <= n < 100): "))
    if n < 4 or n >= 100:
        print("n must be between 4 and 99")
    else:
        result = look_and_say_middle_two(n)
        print(f"The middle two digits of term {n} are: {result}")
