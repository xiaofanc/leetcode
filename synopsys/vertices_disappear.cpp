// undirected graph with N nodes, numbered from 0 to N-1, connected with M edges
// A pair(A[k], B[k]) is an edge
// Each second, every node with at most one edge connects to it disappears. Every edge which is connected to one of the disappearing vertices also disappears.
// After how many seconds will the vertices stop disappearing?
// python: node degree with deque: leetcode 210

#include <vector>
#include <iostream>
#include <map>
#include <iterator>
#include <set>
#include <algorithm>

int solution(int N, std::vector<int> &A, std::vector<int> &B) {
	std::map<int, std::vector<int>> m;
	// create a map for the edges
	for (unsigned int i = 0; i < A.size(); i++) {
		m[A[i]].push_back(B[i]);
		m[B[i]].push_back(A[i]);
	}
	// number of nodes without edges
	int singlenode = N - m.size();

	std::vector<int> removedkeys;
	std::vector<int> removevalues;
	int seconds = 0;
	std::map<int, std::vector<int>>::iterator it;

	while (!m.empty()) {
		// loop over the map and delete vertex with edges <= 1
		for (it = m.begin(); it != m.end();) {
			int vertex = it->first;
			std::vector<int> vertices = it->second;
			// if edges <= 1, then remove the vertex and remember the values
			if (vertices.size() <= 1) {
				it = m.erase(it);
				if (!vertices.empty()) {
					removedkeys.push_back(vertex); // [5, 6]
					removevalues.push_back(vertices.at(0));  // [4]
				}
			} else {
				it ++;
			}
		}

		// check if any keys are removed
		if (!removedkeys.empty() || singlenode >=1 ) {
			seconds += 1;	
			singlenode = 0;
		} else {
			break;
		}

		// remove values in the map before next loop
		it = m.begin();
		while (it != m.end() && !removevalues.empty()) {
			for (unsigned int i = 0; i < removevalues.size(); i++) {
				if (it->first == removevalues.at(i)) {
					it->second.erase(std::remove(it->second.begin(), it->second.end(), removedkeys[i]), it->second.end());			
				}
			}
			it ++;
		}
		removevalues.clear();
		removedkeys.clear();
	}
	// std::cout << "seconds --> " << seconds << std::endl;
	return seconds;
}



int main() {
  std::vector<int> A;
  std::vector<int> B;
  A.push_back(0);
  A.push_back(1);
  A.push_back(2);
  A.push_back(1);
  A.push_back(4);
  A.push_back(4);

  B.push_back(1);
  B.push_back(2);
  B.push_back(0);
  B.push_back(4);
  B.push_back(5);
  B.push_back(6);

  solution(7, A, B);

  // std::vector<int> A;
  // std::vector<int> B;
  // A.push_back(0);
  // A.push_back(1);
  // A.push_back(2);
  // A.push_back(4);
  // A.push_back(5);

  // B.push_back(1);
  // B.push_back(2);
  // B.push_back(3);
  // B.push_back(5);
  // B.push_back(6);

  // std::vector<int> A;
  // std::vector<int> B;
  // A.push_back(0);
  // A.push_back(1);
  // A.push_back(2);
  // A.push_back(3);

  // B.push_back(1);
  // B.push_back(2);
  // B.push_back(3);
  // B.push_back(0);
  // solution(4, A, B);

  return 0;
}