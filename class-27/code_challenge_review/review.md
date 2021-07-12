## Start with:
a = [4,8,23,16,42,15]

### Iteration 1
i = 1 for loop
temp = 8

j=0 while loop
[4,8,23,16,42,15] => 8<4? stop

### Iteration 2
i = 2
temp = a[i] = 23

j=1
23<8? stop

### Iteration 3
i = 3
temp = a[i] = 16

j = 2 while loop
temp < a[j] ? yes
a[j+1] => a[3] = a[2] => a = [4,8,23,23,42,15]

j= 1
temp < a[j]  => 16 < 8 no => stop
a[j+1] = temp => a[2] = 16
a = [4,8,16,23,42,15]




### Iteration 5
i=5
temp = 15

j=4
a = [4,8,16,23,42,42]

j=3
[4,8,16,23,23,42]

j=2
[4,8,16,16,23,42]

j=1
[4,8,15,16,23,42]