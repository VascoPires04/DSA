#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            vector<int> output;
            for(int i=0;i<nums.size();i++){
                for(int j=i+1;j<nums.size();j++){
                    if(nums[j] + nums[i] == target){
                        output.push_back(i);
                        output.push_back(j);
                        break;
                    }
                }
            }
            return output;
        }
    };