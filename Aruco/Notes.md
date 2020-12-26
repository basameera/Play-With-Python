## Usage
Use the py3 venv

## Problems
* The stop zone is too small when the aruco marker is close.
	SOL: Change the stop zone size with aruco area
* Reading images while moving makes it blurry. So, turn for a small time and then stop and then read images.
* Works best when aruco is 1.5 ft away from camera. Otherwise bot keep turing left and right constantly.

## Progress

### 26-12-2020

#### Session 1

* changed max turn speed to 0.15
* removed undist and roi crop. but resize is still there.
* These settings **work**

##### session 2
* added back the undist and roi crop with speed at 0.15
* this does not work. undist is too slow. 

#### session 3
* with session 1 settings
* loop time = 35 ms

#### session 4
* with session 1 settings + no resize
* loop time = 45 ms - **this make no sense**
* looks like loop time is very important for how well it moves. Don't depend on this.
