#include <iostream>
using namespace std;
string eD(string toE) {
	char key = 'K';
	string output = toE;
	for (unsigned int i=0; i<toE.size(); i++) {
		output[i] = toE[i] ^ key; // is the xor operator
	}
	return output;
}
int main() {
	string a = "Linus";
	string b = eD(a);
	cout << b << endl;
	cout << eD(b) << endl;
}