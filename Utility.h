#include <iostream>
#include <ctime>
using namespace std;
#ifndef UTILITY_H_INCLUDED
#define UTILITY_H_INCLUDED
void print(string in) {cout << in;}
void puts(string in) {cout << in << endl;}
void muchputs(string in) {cout << endl << in << endl;}
string XOReD(string toE) {
	char key = 'K';
	string output = toE;
	for (unsigned int i=0; i<toE.size(); i++) {
		output[i] = toE[i] ^ key; // ^ is the xor operator
	}
	return output;
}
int rand(int n) {
	time_t result=time(nullptr);
	int me = int(result) % n;
	return me;
}
double rand(double n) {
	time_t result=time(nullptr);
	double me = int(result) % n;
	return me + (0.1 * me) + (0.01*me) * (int(time(nullptr))%n*0.01);	
}

#endif // UTILITY_H_INCLUDED
