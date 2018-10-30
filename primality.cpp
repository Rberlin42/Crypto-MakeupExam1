#include <iostream>
#include <cstdlib>
#include <cmath>

// Parameter for accuracy of the primality test
// defines the amount of times each number will be checked with Miller-Rabin
#define t 10

// modular exponentiation
// base^exp % mod
unsigned long long int power(unsigned long long int base, unsigned long long int exp, unsigned long long int mod){
	if(exp == 0)
        return 1;

    unsigned long long int z = power(base, exp/2, mod);

    //utilize following property to compute large numbers:
    // (a*b) mod n = ((a mod n) * (b mod n)) mod n
    if(exp % 2 == 0)
    	// z^2 % mod
        return ((z % mod) * (z % mod)) % mod;
    else
    	// (base * z^2) % mod
        return ((base % mod) * (((z % mod) * (z % mod)) % mod)) % mod;
}


//Miller Rabin implementation to check if a number n is prime
//true if probably prime
//false if composite
bool miller_rabin(int n){
	// Find integers k, q, k > 0, q odd, so that (n–1)=2^k * q
	int q = n - 1; 
	int k = 0;
    while (q % 2 == 0) {
    	k++;
        q /= 2;
    }

    //pick a random number a, 1<a<n–1
    int a = (rand() % (n-2)) + 1;
 
    unsigned long long int x = power(a, q, n);
    if(x == 1 || x == n-1)
    	return true;

   	for (int i = 0; i < k; i++){
    	x = power(x, 2, n);
    	q *= 2;

    	if(x == 1)
    		return false;
    	if(x == n-1)
    		return true;
    }

    return false;
}

//g(x, n) = (x^2 + 1) mod n
int g(int x, int n){
	return (x*x + 1) % n;
}

//Euclid's alg
int gcd(int x, int y){
	if(y == 0)
		return x;
	return gcd(y, x % y);
}

//returns a factor of n
//returns -1 if fail
int pollard_rho(int n){
	int x = 2;
	int y = 2;
	int d = 1;
	while(d == 1){
		x = g(x, n);
		y = g(g(y, n), n);
		d = gcd(abs(x-y), n);
	}

	if(d == n)
		return -1;
	else
		return d;
}



int main(){

	int nums[4] = {31531, 520482, 485827, 15485863};
	long double prob = 1 - powl(.25, t);

	//check each number
	for (int i = 0; i < 4; i++) {
		//run the test for t times
		bool prime = true;
		for(int j = 0; j < t; j++){

			if(!miller_rabin(nums[i])){
				//if it ever returns composite, then it is definitely not prime
				prime = false;
				break;
			}
		}

		if(prime){
			std::cout << nums[i] << " is prime with probability " << prob << std::endl;
		}
		else{
			std::cout << nums[i] << " is composite. ";
			
			//find a factor
			int factor = pollard_rho(nums[i]);

			if(factor == -1)
				std::cerr << "Error factoring number" << std::endl;
			else
				std::cout << "It has a factor of " << factor << std::endl;
		}
			
	}

	return 0;
}