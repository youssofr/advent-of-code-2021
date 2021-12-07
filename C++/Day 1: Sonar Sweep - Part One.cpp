#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string file_name_prefix = "../Inputs/";


int main(){

    // READ DATA FROM FILE TO ARRAY 
    // file srteam to handle input from the file
    ifstream inputs_file;
    inputs_file.open(file_name_prefix.append("Day 1: Sonar Sweep - Part One.txt"));

    // string to read in inputs
    int depths[2000];

    int n_lines = 0;
    // read from file stream object to string
    for (int i = 0; i < 2000 && inputs_file; i++){
        inputs_file >> depths[i];
        n_lines++;
    }
    inputs_file.close();


    // CACULATE ANSWER
    // problem parameter
    int answer = 0;

    for (int i = 1; i < 2000; i++){
        if (depths[i] > depths[i-1])
            answer++;
    }
    
    cout << answer << "\n";

    return 0;
}