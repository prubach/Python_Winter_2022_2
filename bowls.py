#    * * * * * *
#     * * * * *
#      * * * *
#       * * *
#        * *
#         *


# sum the number of bowls given the number of rows (n)

def sum_bowls_loop(rows):
    i = 1
    bowls = 0
    while i < rows:
        bowls += i
        i += 1
        if i == rows:
            bowls += i
            return bowls


def sum_bowls_loop2(rows):
    s = 0
    for i in range(1, rows+1):
        s += i
    return s


def sum_bowls_recursive(n):
    if n==1:
        return 1
    else:
        s = n + sum_bowls_recursive(n - 1)
        return s


def sum_bowls_seq(n):
    return int(n*(n+1)/2)

if __name__ == '__main__':
    #n = 6
    #print('Sum bowls using loop: {} = {}'.format(n, sum_bowls_loop(n)))
    n = 7
    print('Sum bowls using loop: {} = {}'.format(n, sum_bowls_loop(n)))
    print('Sum bowls using loop2: {} = {}'.format(n, sum_bowls_loop2(n)))
    print('Sum bowls using recursion: {} = {}'.format(n, sum_bowls_recursive(n)))
    print('Sum bowls using sequence: {} = {}'.format(n, sum_bowls_seq(n)))
