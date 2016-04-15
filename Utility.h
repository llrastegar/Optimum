#include <iostream>
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
		output[i] = toE[i] ^ key; // is the xor operator
	}
	return output;
}
#endif // UTILITY_H_INCLUDED