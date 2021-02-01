
def qw(n):
    if n<=1:
        return 1
    elif n==2:
        return 2
    else:
        return qw(n-1)+qw(n-2)

if __name__ == "__main__":
    n=7
    print(qw(7))