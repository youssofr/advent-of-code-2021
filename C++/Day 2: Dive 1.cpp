#include <iostream>
#include <fstream>
#include <map>
#include <array>

using namespace std;

string file_name_prefix = "../Inputs/";

int main(){

    // read and solve puzzle
    ifstream input(file_name_prefix.append("Day 2: Dive.txt"));

    map<string,array<int,2>> directions;
    
    directions["forward"] = {1, 0};
    directions["down"] = {0, 1};
    directions["up"] = {0, -1};

    int coordinates[2] = {-9, 0};   // initialized with the inverse of last line
                                    // to overcome the duplicated final ifstream
                                    // TODO : refactor input stream
    string in_direct = "";
    int amount = 0;

    while(input){
        input >> in_direct >> amount;
        coordinates[0] += (directions[in_direct][0] * amount );
        coordinates[1] += (directions[in_direct][1] * amount );
    }

    cout << coordinates[0] * coordinates[1] << endl;

    return 0;
}