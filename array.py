'''2.	Write a program to accept a two-dimensional array containing integers as the parameter and determine the following from the elements of the array:
a.	Element with minimum value in the entire array
b.	Element with maximum value in the entire array
c.	The elements with minimum and maximum values in each column
d.	The elements with minimum and maximum  values in each row'''


n = 4
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(0, i):
        a[i][j] = 2
    a[i][i] = 1
    for j in range(i + 1, n):
        a[i][j] = 0
for row in a:
    print(' '.join([str(elem) for elem in row]))