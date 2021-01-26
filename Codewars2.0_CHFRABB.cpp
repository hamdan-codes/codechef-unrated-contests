
#include <bits/stdc++.h>
using namespace std;

int max(int x, int y)
{
	return (x > y) ? x : y;
}

int minJumps(int arr[], int n)
{

	if (n <= 1)
		return 0;

	if (arr[0] == 0)
		return -1;

	int maxReach = arr[0];

	int step = arr[0];
	int jump = 0;

	int i = 1;
	for (i = 1; i < n; i++) {
		if (i == n - 1)
			return jump + 1;

		maxReach = max(maxReach, i + arr[i]);

		step--;

		if (step == 0) {
			jump++;

			if (i >= maxReach)
				return -1;

			step = maxReach - i;
		}
	}

	return -1;
}

int main()
{
	int t; cin >> t;
	while (t--)
	{
		int size; cin >> size;
		int arr[size];
		for (int i = 0; i < size; i++)
			cin >> arr[i];
		cout << minJumps(arr, size) << endl;
	}

	return 0;
}
