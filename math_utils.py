# Giữ lại hàm is_prime cũ...

def find_primes_in_range(limit):
    """Hàm tìm tất cả các số nguyên tố từ 2 đến limit"""
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Chạy thử nghiệm bổ sung
limit = 20
print(f"Các số nguyên tố từ 1 đến {limit} là: {find_primes_in_range(limit)}")