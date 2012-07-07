#include <string>

// Statics
static const int WAVELENGTHS = 7;
constexpr static const char* COLOURS[WAVELENGTHS] = {"#red", "#orange", "#yellow", "#green", "#blue", "#indigo", "#purple"};

// Functions
std::string colourise(char c, int i);
std::string rainbow(std::string line, int offset);

