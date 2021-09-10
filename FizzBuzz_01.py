# Fizz Buzz - Brenton Wright - September 2021

# Start counting from 1
# If number is divisible by 3, print "Fizz"
# if number is divisible by 5, print "Buzz"
# if number is both divisible by 3 and 5, print "FizzBuzz"
# otherwise print the number.

fb_seq = []
fb_size = 30
count = 1

while count <= fb_size:
    if count % 3 == 0 and count % 5 != 0:
        fb_seq.append("Fizz")
        count += 1
    elif count % 5 == 0 and count % 3 != 0:
        fb_seq.append("Buzz")
        count += 1
    elif count % 3 == 0 and count % 5 == 0:
        fb_seq.append("FizzBuzz")
        count += 1
    else:
        fb_seq.append(count)
        count += 1
print(fb_seq)
