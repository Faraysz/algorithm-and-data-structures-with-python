def bin_search(nums,x):
  low, high = 0, len(nums) - 1 # menginisialisasikan titik low dan high 
  while low <= high:
    mid = (low + high) // 2 # mendeklarasikan titik mid
    if nums[mid] == x:
      return mid
    elif nums[mid] > x:
      high = mid -1
    else:
      low = mid + 1
  
  return -1 # apabila result tidak ditemukan


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 7
    index = bin_search(data, target)
    if index != -1:
        print(f"{target} ditemukan pada indeks {index}")
    else:
        print(f"{target} tidak ditemukan")