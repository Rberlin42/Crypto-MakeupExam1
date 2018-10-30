# Makeup Exam 1

## Part 1

For part 1, my collision attack program is in the file collision_attack.py. The program 
demonstrates how a collision attack would work, by finding a common hash value for a legitimate
message and a fraudulent message.  The legitimate message is the excerpt provided on the assignment, 
and for the fraudulent message I used a paragraph from the textbook.  For this program I used a 
hash size of 32 bits, and so therefore it computed 2^16 variations of each message, giving us a .5 
probability of finding a collision.

The program begins by generating all variations of the legitimate message, and then hashes each message.
It then does the same for the fraudelent messages, however after each message it hashes, it will check if
there is a collision.  Upon finding a collision, the program will output both messages and their hash value.

## Part 2

My part 2 solutions are found in Part 2.pdf.  I did this assignment on the global version of the textbook
before realizing that some of the numbers in the questions were different.  The questions themselves are the
same, so hopefully this will suffice.

## Part 3

My Part 3 implementation is in the file primality.cpp.  The numbers we needed to check are hard-coded in 
for simplicity. Upon compiling and running the program, it will check if each number is prime using the
Miller-Rabin algorithm, and if it is composite, it will then show one of its factors using the Pollard-Rho method.
My program runs the Miller-Rabin algorithm on each number 10 times, and computes the probablility that the 
number is prime. Since the numbers are fairly large, I also implemented a modular exponentiation function to 
aid with the computation.

Answers:</br>
31531 is prime with probability 0.999999</br>
520482 is composite. It has a factor of 3</br>
485827 is prime with probability 0.999999</br>
15485863 is prime with probability 0.999999
