#include <stdio.h>
#include <iostream>
#include <vector>
#include <chrono>
#include <thread>

using namespace std;

int main() {
    int cases;
    cin >> cases;

    cout << "cases: " << cases << endl;

    for (int c = 0; c < cases; c++) {
        long start;
        cin >> start;
        int times;
        cin >> times;

        vector<long> values;
        for (int i = 0; i < times; i++) {
            long value;
            cin >> value;
            values.push_back(value);
        }

        long curr = start;
        for (int i = 0; i < ((int) values.size()) - 1; i++) {
            if (values[i + 1] > values[i] && values[i] != 0) {
                curr += (values[i + 1] - values[i]) * (curr / values[i]);
            }
        }
        cout << c + 1 << " " << curr << endl;

        this_thread::sleep_for(1s);
    }

    return 0;
}
