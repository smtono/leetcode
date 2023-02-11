#include <vector>
#include <unordered_map>

class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            std::vector<int> solution;
            std::unordered_map<int, int> values; // Creating a hash map initialized with nums values
            int difference;

            for (int i = 0; i < nums.size(); i++) {
                difference = target - nums[i]; // Start by finding the difference right away so we know what to look for
                if (values.find(difference) != values.end() && values.find(difference)->second != i) { // making sure not out of bounds, and also not a duplicate
                    solution.push_back(i); // push the element we are on
                    solution.push_back(values.find(difference)->second); // push the pair that adds up to the target which is the difference
                    break;
                }
                else { // if it is not found then we need to store this element into the map
                values[nums[i]] = i;
                }
            }
            return solution;
        }
};