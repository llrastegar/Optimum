
#include <iostream>
#include <string>
#include <bitset>
#include <vector>
using namespace std;

void print(string str) {cout << str;}
void puts(string str) {cout << str << endl;}
void print(char str) {cout << str;}
void puts(char str) {cout << str << endl;}
string ConvertToBinary(int n) { return bitset<8>(n).to_string(); }
unsigned long ConvertToDec(string binary) { unsigned long decimal = std::bitset<8>(binary).to_ulong(); return decimal;}
int main() {
	string tst = "Linus n'aime pas les Francais";
	//----Encrypting from here:
	int arr[tst.size()];
	vector <string> binaries;
	for (int i=0; i<=tst.size()-1; i++) {
		arr[i] = tst[i];
		binaries.push_back(ConvertToBinary(arr[i]));
		puts(binaries[i]);
	}
	//----Decrypting from here:
	string n_tst;
	int narr[tst.size()];
	for (int i=0; i<=tst.size()-1; i++) {
		narr[i] = ConvertToDec(binaries[i]);
		char a = narr[i];
		n_tst+= a;
	}
	puts("-----------"); puts(n_tst);
	//now we have the array of binaries, ord numbers, and actual string
	//we need to convert to ternary correctly, and encrypt from there, as well as decrypt
}
