def fibonnaci(n):
  if (n <= 2):
    return 1
  return fibonnaci(n-1) + fibonnaci(n-2)

if __name__ == "__main__":
  import sys
  print fibonnaci(int(sys.argv[1]))