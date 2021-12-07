#include <fstream>
#include <iostream>

using namespace std;

string file_name_prefix = "../Inputs/";

int main(){

    // read input

    ifstream input(file_name_prefix.append("Day 1: Sonar Sweep - Part Two.txt"));

    // problem parameters
    const int stride = 3;
    int depths[stride];
    int aggrg = 0, last_aggrg = 0;

    // final answer
    int answer = 0;

    int i = 0;
    while(input){
        // read in input
        input >> depths[i%stride];
        
        // calculate new aggregate
        if (i >= 2){
            aggrg = 0;
            for (int j = 0; j < stride; j++)
                aggrg += depths[j];
        }
        // check condition and increment answer
        if (i > 2 && last_aggrg < aggrg)
            answer++;
        // update parameters
        last_aggrg = aggrg;
        i++;
    }

    cout << answer << "\n";

    return 0;
}