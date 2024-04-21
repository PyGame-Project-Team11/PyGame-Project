# UniPixiLife
### ***UniPixiLife*** is an exciting game where the player in the role of a student must go through 15 weeks of study, coping with various challenges and mini-games. Faced with the challenges of study, social life and finance, the player must manage his budget, take care of his health and build relationships with friends in order to complete the game successfully. A fascinating immersion into the life of a student, where every decision matters!
### Objective: Go through 15 weeks(specific days) of study, managing your budget, health and social life. Make decisions and go through mini-games.


## Running the game
### To run the game you will need the pygame and python (3.6-newer versions) to be installed, also assets (images) from the repository. 

```python
python3 main.py
```

### To start the game,  ```game.py``` file should be executed
```python
py game.py
```
## Code
#### Libraries: ```pygame```, ```time```,```random```

```python
def __init__(self): 
```
#### initializes a new instance of the Player class
```python
def draw_stats(self,screen):
```
#### Draws the player's statistics on the screen
```python
def is_inside(rect, pos):
```
#### Checks if a given position is inside a rectangle
```python
def show_rules():
```
#### Displays the rules of the game on the screen
```python
def background_change(n):
```
#### Changes the background
```python
def blackout():
```
#### 1. ```while running:``` controls the flow of the game
#### 2.Event handling ```pygame.event.get()```
#### 3. 9 days of the game
#### 4.```blackout()``` filling screen with black, simulating a transition between events
