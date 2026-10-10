#include <iostream>  // Required for input and output operations
#include <string>    // Required to use the string data type

int main() {
    // 1. Output a simple message
    std::cout << "Welcome to C++ Programming!" << std::endl;

    // 2. Variables and User Input
    std::string userName;
    std::cout << "Enter your name: "
    std::cin >> userName; // Reads a single word from the user

    int num1, num2;
    std::cout << "Enter two integers separated by a space: ";
    std::cin >> num1 >> num2; // Reads two integer values

    // 3. Basic Arithmetic
    int sum = num1 + num2;

    // 4. Display Results
    std::cout << "\nHello, " << userName << "!" << std::endl;
    std::cout << "The sum of " << num1 << " and " << num2 << " is: " << sum << std::endl;

    return 0; // Signals that the program executed successfully
}
