#include <iostream>
using namespace std;

int main() {
  cout << "  **** CALCULATE TEMPERATURE ****" << endl;
  cout << "Select the temperature unit:" << endl;
  cout << "1.  Celcius" << endl;
  cout << "2.  Fahrenheit" << endl;
  cout << "3. Kelvin" << endl;

  int sayi;
  cout << "Please enter your selection (1-3): ";
  cin >> sayi;

  switch (sayi) {
    case 1: {
      double celcius;
      cout << "Enter the temperature in Celsius: ";
      cin >> celcius;
      double fahrenheit = celcius * 9.0 / 5.0 + 32;
      double kelvin = celcius + 273.15;
      cout << celcius << " °C = " << fahrenheit << " °F, " << kelvin << " K" << endl;
      break;
    }
    case 2: {
      double fahrenheit;
      cout << "Enter the temperature in Fahrenheit: ";
      cin >> fahrenheit;
      double celcius = (fahrenheit - 32) * 5.0 / 9.0;
      double kelvin = celcius + 273.15;
      cout << fahrenheit << " °F = " << celcius << " °C, " << kelvin << " K" << endl;
      break;
    }
    case 3: {
      double kelvin;
      cout << "Enter the temperature in Kelvin: ";
      cin >> kelvin;
      double celcius = kelvin - 273.15;
      double fahrenheit = celcius * 9.0 / 5.0 + 32;
      cout << kelvin << " K = " << celcius << " °C, " << fahrenheit << " °F" << endl;
      break;
    }
    default:
      cout << "Invalid selection. Please choose 1, 2, or 3." << endl;
      break;
  }

  return 0;
}