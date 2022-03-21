// source: https://en.wikipedia.org/wiki/Knapsack_problem
// used this wikipedia article to think about knapsack in a different way

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

int max(int a, int b) {
     if (a > b) {
          return a;
     }
     else {
          return b;
     }

}

int Dynamicknapsack(int weight_arr[], int price_arr[], int num_items, int max_weight, vector<int> &v) {
     // converted from python code in previous implementation into c++
     int table[num_items + 1][max_weight + 1]; // initialize table
     for (int i = 0; i <= num_items; i++) { // outer loop to num items
          for (int j = 0; j <= max_weight; j++) { // inner loop to max weight
              if (i == 0 || j == 0) { // case where its the first row and col
                   table[i][j] = 0;
              }
              else if (weight_arr[i - 1] <= j) { // case where weight can be added and it increases the max price
                   table[i][j] = max(price_arr[i - 1] + table[i - 1][j - weight_arr[i - 1]], table[i - 1][j]);
              }
              else{ // o/w, take the value to the top left
                   table[i][j] = table[i - 1][j];
              }
          }
     }
     
     int max = table[num_items][max_weight]; // grab the max
     int k = max_weight;

     for (int i = num_items; i > 0 && max > 0; i--) { // while there is still items to run through
          if (max == table[i - 1][k]) {
              continue;
          }
          else { // add the new max to the vector
              v.push_back(i);
              max -= price_arr[i - 1];
              k -= weight_arr[i - 1];
          }
     }
     return table[num_items][max_weight]; // return this new max
}

int main() {

     int num_tests, num_items, price_arr[500], weight_arr[500], fam_mems, max_weight;

     vector<vector<int> > vec(100); // initialize the vector
     ifstream inf; // objects for writing to and reading from files
     ofstream outf;

     inf.open("shopping.txt"); // open the input file
     outf.open("extra.out"); // open the output file

     inf >> num_tests; // get the number of tests

     for (int k = 0; k < num_tests; k++) { // loop through the number of tests

          inf >> num_items; // get the number of items
          for (int i = 0; i < num_items; i++) { // take in their prices and weights
              inf >> price_arr[i];
              inf >> weight_arr[i];
          }
          int max_p = 0; // initialize this max for the weight carried
          inf >> fam_mems; // get the number of family members
          for (int j = 0; j < fam_mems; j++) { // loop through the fam members
              inf >> max_weight; // take in their max weight
              max_p = max_p + Dynamicknapsack(weight_arr, price_arr, num_items, max_weight, vec[j]); // add the most value that they can carry
          }

          outf << "Total Price " << max_p << endl; // printing data to the outfile
          outf << "Member Items" << endl;
          cout << "Total Price " << max_p << endl;
          cout << "Member Items" << endl;
          
          // now for the vectors to keep track of the weight per person
          for (int j = 0; j < fam_mems; j++) {
              sort(vec[j].begin(), vec[j].end()); // ensure that they come out in the correct order
              outf << j + 1 << " : "; // printing the num
              cout << j + 1 << " : ";
              for (int k = 0; k < vec[j].size(); k++) { // printing all the weights
                   outf << vec[j][k] << " ";
                   cout << vec[j][k] << " ";
              }
              cout << endl; // print endlines
              outf << endl;
          }
     }
     // close files
     inf.close();
     outf.close();

     return 0;
}