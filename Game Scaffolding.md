# Class Manager
Contains a function that draws
* Instructions screen
* highscore screen
* Current game/screen to display

 ### Contains the game class, which 
    * Contains the power pellet timer function
 * Contains the **player class**

    -Player class contains;
    * The score
    * Player's name
    * Lives remaining
    * Player inputs
    * Pacman maybe..?
    
* Contains **level class**
    * has a number(determining the level)
        * has a movement speed(increases as the level number is higher)
    * Contains the **maze/grid class**
        * Contains an array of all items in the 'Grid Item" Class.
            **Grid item class** contains:
            * Animation
            * Coordinates
            * On collision behaviour
            * Disappear
            * Deny collision for:?????

            
            * visibility
        ---
* Fruits eaten
* The Ghost class which contains
    * Inherits from the Entity class containing
        * Animation
        * Movement speed
        * Position
        * Direction currently moving
        * Collisions class
            * On movement, check if inside wall
            - if so, return to original positions
        * "Super pellet mode"
        * Control scheme
        * Dead/alive state
    * A control scheme
    * 3 modes; Chase, scatter, frightened
    * Kill pacman on collision
    * Release time on game start
* On game over:submit score to evaluate for high score
        ### Contains Instructions 