# MA1 Physics 1

My first Physics I major assignment in college as a freshman <br />
Faculty of Computer Science and Engineering, Ho Chi Minh University of Technology

# Brief topic walkthrough

Spacecraft ejects its burned fuel, which causes itself to move upward as well as losing its weight. <br />
Given the `v'` as speed of fuel ejection, `dm/dt` as burning rate, `m0` as inital mass and `y0` as inital coordinate. <br />
Solve the equation `mdv/dt = - v'dm/dt - mg`, we will have acceleration, velocity and coordinate. <br />
Plot the function y(t) on matlab using symbolic package.

# Solving

Because m decreases over time, `dm/dt` is less than 0, we call it `k` for simplification (`k` < 0). <br />
We have acceleration equation as `a = dv/dt`, we can compute both velocity and coordinate equation by integration. <br />
We choose the positive direction upward, which means `g` and `v'` are negative.
