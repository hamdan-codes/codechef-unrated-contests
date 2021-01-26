#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
	int digitCount(int x) {
		int ret = 0;
		while (x) {
			ret++;
			x /= 10;
		}
		return ret;
	}
	int zero(int n) {
		int ret = 0;
		int x = 0;
		if (n == 0)
			return 1;
		for (int m = 1; m <= n; m *= 10) {
			int a = n / m;
			int b = n % m;
			int z = a % 10;
			if (digitCount(m) == digitCount(n))
				break;
			if (z > x) {
				ret += ((a / 10) + 1) * m;
			}
			else if (z == x) {
				ret += (a / 10) * m + (b + 1);
			} else {
				ret += (a / 10) * m;
			}
			cout << ret << endl;
		}
		return ret;
	}
	int f(int x, int n) {
		int ret = 0;
		for (int m = 1; m <= n; m *= 10) {
			int a = n / m;
			int b = n % m;
			int z = a % 10;
			if (z > x) {
				ret += ((a / 10) + 1) * m;
			}
			else if (z == x) {
				ret += (a / 10) * m + (b + 1);
			} else {
				ret += (a / 10) * m;
			}
			if (x == 0) {
				ret -= m;
			}
		}
		return ret;
	}
	int digitsCount(int d, int low, int high) {
		return f(d, high) - f(d, low - 1);
	}
};
int main() {
	int t; cin >> t;
	while (t--)
	{

		int a, b; cin >> a >> b;

		Solution ob;
		cout << (ob.digitsCount(7, a, b)) << endl;
	}

}