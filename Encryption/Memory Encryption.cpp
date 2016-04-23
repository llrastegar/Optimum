#include <iostream>
#include "Cryptoheader.h"
using namespace std;
int main() {
	string encrypt = "Fencing";
	string *str;
	str = &encrypt;
	cout << str << endl;
	print(encrypt);
}
