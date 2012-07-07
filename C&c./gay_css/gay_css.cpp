#include <iostream>
#include <string>
using namespace std;
#include "rainbow.h"

int main()
{
    const string test_string = "Rowsdower";
    int offset = 0;
    string output = rainbow(test_string, offset);

    cout << output << '\n';
}

