#include <string>
#include <cctype>
#include <iostream>
using namespace std;
#include "rainbow.h"

string colourise(char c, int i)
{
    return string(COLOURS[i]) + c;
}

string rainbow(string line, int offset)
{
    int i = (0 + offset) % 7;
    //int count = 0;
    string new_line = "";
    //for char in line:
    for (string::iterator n = line.begin(); n != line.end(); n++)
    {
        //char c = *n;
        if ( isspace(*n) )
        {
            new_line += *n;
        }
        else
        {
            new_line += colourise(*n, i);
            //count += 1;
            i = (i + 1) % 7;
        }
    }
    return new_line;
}

