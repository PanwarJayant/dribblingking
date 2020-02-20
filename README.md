# dribblingking
This is an arcade dribbling football game developed on Python with pygame library.   
**BEFORE PLAYING:**  
Make sure you have python and pygame libraries installed on your system.   
Then, clone this repository on your system and run gamepul.py file. Make sure you clone it as it is and not make any changes to the tree structure of the repository.   
**HOW TO PLAY:**  
This is a multiplayer game. So two players can play this at the same time.   
Player1 dribbles from the bottom to the top of the screen while Player2 dribbles from the top to the bottom of the screen.   
If you reach the end of the screen for the particular player, you level up and the other Player gets their chance. In case, the latter had collided with any defenders before, then the former continues on to the next level.   
**SCORING:**  
For getting past a line of standing defenders successfully, Player earns 5 points and for getting past a line of sliding defenders they earn 10 points.  
Timing also plays an important role in scoring. The total score of a level is calculated by subtracting the timing from the earned score. For the first level, the time is subtracted as it is from the score and from thereon, only a fraction of the time taken is subtracted from the score. The greater the level, the less time is subtracted from the total score.  
The score keeps on adding as the Player keeps on completing the levels.  
**WINNING:**  
The winner is calculated based on which player went further in levels.  
If the two players went till the same level, then their score is used to check for tie breaking.  
If the players have both same level and scores, then the game is declared as a tie.
