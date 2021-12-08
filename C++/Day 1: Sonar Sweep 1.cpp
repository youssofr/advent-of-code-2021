#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string file_name_prefix = "../Inputs/";


int main(){

    // file srteam to handle input from the file
    ifstream inputs_file;
    inputs_file.open(file_name_prefix.append("Day 1: Sonar Sweep - Part One.txt"));

    // int array to save last and current depths to compare as file is read
    int depths[2];
    int answer = 0;
    // read from file stream object to string
    int i = 0;
    while (inputs_file){
        inputs_file >> depths[i%2];
        if (i > 0 && depths[i%2] > depths[(i-1)%2])
            answer++;
        i++;
    }
    inputs_file.close();
    
    cout << answer << "\n";


    return 0;
}