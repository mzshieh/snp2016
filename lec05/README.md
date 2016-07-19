## Lecture 5

### Review

+   Built-in events do more
    +   Delay
    +   Block
    +   Cancel
+   Alternatives
    +   Infinite loops
    +   Broadcast
+   Design and reuse
    +   Precondition
        +   What we need to put before the designed command
    +   Postcondition
        +   What we get after executing the command
    +   [Example 1](https://scratch.mit.edu/projects/115904117/)
        +   draw a filled triangle
            +   Precondition
                +   None
            +   Postcondition
                +   Effect: draw a filled triangle in green
                +   Side effect
                    +   Move the sprite to (x3,y3)
                    +   Pen up
                    +   Set pen size to 10
                    +   Set pen color to green
    +   [Example 2](https://scratch.mit.edu/projects/115838437/)
        +   draw the crown
            +   Precondition
                +   Sprite must be at (0,-50)
                +   Sprite must face 0 degree (up)
            +   Postcondition
                +   Effect
                    +   Draw 5 green circles at the desired positions if the precondition is satisfied.
                +   Side effect
                    +   Move the sprite to (0,0)
                    +   The sprite will face 75 degrees
    +   [Example 3](https://scratch.mit.edu/projects/115835376/)
        +   draw a tree of trunk size toward relative angle (rooted at sprite's current position)
            +   Precondition
                +   None
            +   Postcondition
                +   Effect
                    +   Draw a leaf if trunk size is less than 5.
                    +   Otherwise, draw a tree rooted at sprite's current position.
                +   Side effect
                    +   Set pen color
                    +   Set pen size
                    +   Pen up
+   Task
    +   Draw a snowflake
    +   Optional: [Draw a Koch snowflake](https://en.wikipedia.org/wiki/Koch_snowflake)
+   Decomposition
    +   Divide and conquer
    +   Incremental
        +   Example: [Insertion sort](https://scratch.mit.edu/projects/116187770/)
        +   Loop invariants
            +   In iteration m, the first m items are sorted.

### Game

+   [Maze](https://scratch.mit.edu/projects/11414041/)
+   [Pong](https://scratch.mit.edu/projects/10128515/)
+   [Scrolling](https://scratch.mit.edu/projects/22162012/)
+   [Fish Chomp](https://scratch.mit.edu/projects/10859244/)
+   Puzzles
    +   Whenever you press the B key, the sprite gets a little bigger. Whenever you press the S key, the sprite gets a little smaller.
    +   Whenever the sprite hears a loud sound, it changes color.
    +   Whenever the sprite is in the top 25% of the screen, it says "I like it up here."
    +   When the sprite touches something blue, it plays a high note. When the sprite touches something red, it plays a low note.
    +   Whenever two sprites collide, one of them says: "Excuse me.”
    +   Whenever the cat sprite gets near the dog sprite, the dog turns and runs from the cat.
    +   Whenever you click on the background, a flower appears at that spot.
    +   Whenever you click on a sprite, all other sprites do a dance.
    +   Whenever you move the mouse-pointer, the sprite follows but doesn't touch the mouse-pointer.
+   [Debug It!](https://scratch.mit.edu/studios/475634/)
    +   [Debug 4.1](https://scratch.mit.edu/projects/24271192/): Scratch Cat 只能撿起筆記型電腦到 Inventory ，請修改程式讓他可以撿起其他東西。
    +   [Debug 4.2](https://scratch.mit.edu/projects/24271303/): 請改到讓 Scratch Cat 碰到黃色 Gobo 時加 10 分，碰到粉紅 Gobo 時減 10 分。
    +   [Debug 4.3](https://scratch.mit.edu/projects/24271446/): 請修好這個猜數字遊戲，讓 Scratch Cat 不要在那邊胡說八道。
    +   [Debug 4.4](https://scratch.mit.edu/projects/24271475/): 請讓球打到 Scratch Cat 一次時，# of hits 只增加 1。
        +   額外要求：讓畫面上有 10 顆球在飛。
        +   Hint: Clone, 分身。
    +   [Debug 4.5](https://scratch.mit.edu/projects/24271560/): 請修改成不會穿過綠色怪物的版本。

### Scratch Extension

+   Download your Scratch project
+   Upload your Scratch project to [ScratchX](http://scratchx.org/)
+   Experimental blocks
    +   Speech
    +   Internet
    +   Hardware
        +   Arduino
        +   Lego