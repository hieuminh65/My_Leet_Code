#include <iostream>
#include <cstdio>
#include <string>
#include <stack>
using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        string result;
        stack <char> tempst;
        int i = s.length() - 1;
        while (i >= 0) {
            if (s[i] == ' '  && !tempst.empty()) {
                    while (!tempst.empty()){
                        result += tempst.top();
                        tempst.pop();
                    }
                    result += " ";
                }
            else if (s[i] == ' '  && tempst.empty()) {
                i--;
                continue;
            }
            else {
                tempst.push(s[i]);
            }
            i--;
        }    

        while (!tempst.empty()) {
            result += tempst.top();
            tempst.pop();
        }
        while (result.back() == ' '){
            result.pop_back();
        }
        return result;
    }
};

int main(){
    Solution sol;
    string s = "  hello world  ";
    cout << "||" <<sol.reverseWords(s) << "||" << endl;
    return 0;
}