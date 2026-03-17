S = [11,17,26,28,37,45,53,59]


def bin_search(nums, x):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == x:
            return mid
        elif nums[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return -1


x = int(input("Masukan nomor yang ingin dicari: "))

pos = bin_search(S, x)  # fungsi untuk binary search
if pos != -1:
    print(f"Posisi bilangan {x} didalam list S adalah posisi nomor {pos}")
else:
    print(f"Bilangan {x} tidak ditemukan dalam list S")