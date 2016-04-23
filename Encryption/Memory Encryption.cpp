#include <iostream>
#include "Utility.h"
using namespace std;
int main() {
	string encrypt = "Fencing";
	string *str;
	str = &encrypt;
	cout << str << endl;
	print(encrypt);
}
