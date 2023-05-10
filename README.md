# ConvexHull-GrahamScan

# Description
The convex hull of a set of points is the set of all possible convex combinations formed by the points. Graham Scan is an algorithm for finding the convex hull of a finite set of points. The algorithm is performed through the following steps:
1. A starting point is found by finding the point in the set with the smallest y value. If there is a tie, the one with the smallest x value will be taken.
2. The rest of the points are ranked according to their polar angle with respect to the starting point $(x_{1}, y_{1})$. In the result of a tie, the farthest point is taken and the rest are removed. The polar angle is found by the equation: 
$$\theta =\arctan\frac{y_{2} - y_{1}}{x_{2} - x_{1}}$$
4. Points are considered sequentially. Points which form a left-handed or counter-clockwise turn will be added to the convex hull perimeter but those which form a right-handed or clockwise turn will be removed. A left-hand turn is defined for 3 points when: 
$$( x_{2} - x_{1} )( y_{3} - y_{1} ) -  ( y_{2} - y_{1} )( x_{3} - x_{1} )  > 0$$
The Graham Scan algorithm has time complexity O(n log n)

---
# Organization

## Tree
```bash
code
   |-- convexhullvis.py
   |-- runtimevis.py
results
   |-- n5_convexhull.png
   |-- n50_convexhull.png
   |-- n500_convexhull.png
   |-- runtime.png
```
# Running the project

To run the project download the repository and run:
```
python3 convexhullvis.py
```
You will then be prompted to enter the desired number of points to be randomly generated and visualized. Once picked the program will run and generate the visualization in a separate window.

To generate an analysis on the runtime complexity of the algorithm download the repository and run:
```
python3 runtimevis.py
```
---
# Results

n = 5                      |  n = 50                   | n = 500
:-------------------------:|:-------------------------:|:-------------------------:|
![](https://github.com/CameronKerr/ConvexHull-GrahamScan/blob/main/results/n5_convexhull.png)  |  ![](https://github.com/CameronKerr/ConvexHull-GrahamScan/blob/main/results/n50_convexhull.png) | ![](https://github.com/CameronKerr/ConvexHull-GrahamScan/blob/main/results/n500_convexhull.png)

![](https://github.com/CameronKerr/ConvexHull-GrahamScan/blob/main/results/runtime.png)
