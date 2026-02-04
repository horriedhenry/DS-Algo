#include <iostream>
#include <vector>

void swap(int& a, int& b) {
    int tmp {b};
    b = a;
    a = tmp;
}

void bubble_sort(std::vector<int>& vec)
{
    int len = vec.size();
    int tmp{0};
    int cur{0};
    int nxt{0};
    for (int i = 1; i < len; i++) {
        for (int j = 0; j < len - i; j++) {
            if (vec[j] > vec[j + 1]) {
                swap(vec[j], vec[j + 1]);
            }
        }
    }
}

void bubble_sort_v2(std::vector<int>& vec) {
    int len = vec.size();
    
    for (int i = 0; i < len; i++) {
        for (int j = 0; j < len - 1 - i; j++) {
            if (vec[j] > vec[j + 1]) {
                swap(vec[j], vec[j + 1]);
            }
        }
    }
}

int main (int argc, char *argv[])
{
    std::vector<int> vec {5, 4, 3, 2, 1, 0};

    bubble_sort_v2(vec);
    
    for (auto num : vec) {
        std::cout << num << " ";
    }
    std::cout << "\n";
}
