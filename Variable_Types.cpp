#include <iostream>
#include "Header.h"
using namespace std;

void print(string a) { cout << a; }
void print(char a) { cout << a; }
void puts(string a) { cout << a << endl; }
void puts(char a) { cout << a << endl; }

class Error {
    string type;
    string name;
    static Error error_array[5];
    Error (string n, string t) : type(t), name(n) {}
};

class Str {
public:
    string str;
    char head, tail;
    unsigned int length;
    Str(string s) : str(s), length((short)s.length()), head(s[0]), tail(s.back()) {}
    int find(char f) {
        for (int i = 0; i<=length-1; ++i) {
            if (str[i]==f) return i;
        }
        return -1;
    }
    char at(int index) {
        if (index>length-1) index%=length;
        return str[index];
    }
    Str operator + (const Str &s) {
        Str l(str + s.str);
        return l;
    }
    Str operator + (const string &s) {
        Str l(str + s);
        return l;
    }
    Str operator = (const string &s) { Str l(s); return l; }
};

class Num {
public:
    double decimal, integer, floater;
    Str type;
    Num (string num, string type="") : type(type) {
        if (type.compare("")==0) {
            for (int i = 0; i<=num.length()-1; i++) {
                if (num[i]=='.') this->type = "sdouble";
            }
        }
        else if (type.compare("sdouble")!=0 and type.compare("float")!=0 and type.compare("double")!=0) {
            this->type = "int";
            integer = stoi(num);
        }
        else if (type.compare("double")==0) {
            this->type = "double";
            decimal = stod(num);
        }
        else if (type.compare("float")==0) {
            this->type = "float";
            floater = stof(num);
        }
        else if (type.compare("int")==0) {
            this->type = "int";
            integer = stoi(num);
        }
    }
    string get() {
        if (type.str.compare("int")==0 or type.str.compare("sint")==0) return to_string(integer);
        else if (type.str.compare("float")==0) return to_string(floater);
        else if (type.str.compare("double")==0 or type.str.compare("sdouble")==0) return to_string(decimal);
        else return "0";
    }
    Num operator + (const Num& n) {
        Num l("0");
        l.floater += floater;
        l.integer += integer;
        l.decimal += decimal;
        return l;
    }
};



int main() {
    Num l("0");
    Num n("2.4");
    cout << (n+l).decimal;
}






