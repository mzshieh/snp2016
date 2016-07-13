## Lecture 4

### Review

+   [Slide (PDF)](snp_lec04.pdf)
+   [Slide (PowerPoint)](snp_lec04.pptx)
+   Variable
+   List
+   Parallelism
+   `bitmap` versus `vector`
+   Infinite loop caused by bug
+   Event implementation
    +   [Reference](https://wiki.scratch.mit.edu/wiki/When_()_Key_Pressed_(block))
+   Infinite loops may be useful
+   Broadcast -- User defined events and triggers

+   [Debug it!](https://scratch.mit.edu/studios/475539/) [Instructor's solution](https://scratch.mit.edu/studios/2923436/)
    +   [Debug 2.1](https://scratch.mit.edu/projects/23266426/): 希望按下 Scratch Cat 後他會隨鼓聲跳舞，但他沒跳，該怎麼辦？
    +   [Debug 2.2](https://scratch.mit.edu/projects/24268476/): 希望 Nano 被碰到的時候也要說話，該怎麼辦？
    +   [Debug 2.3](https://scratch.mit.edu/projects/24268506/): 希望畫個笑臉，目前有一些地方多畫了，該怎麼辦？
    +   [Debug 2.4](https://scratch.mit.edu/projects/23267140/): 希望花開完了要停下來，該怎麼辦？
    +   [Debug 2.5](https://scratch.mit.edu/projects/23267245/): 希望生日快樂歌唱完才提示可以吹蠟燭了。
+   Trigger
    +   [Event](https://scratch.mit.edu/projects/116182454/)
    +   [Infinite loop](https://scratch.mit.edu/projects/116182906/)
    +   [Broadcast](https://scratch.mit.edu/projects/116183365/)
+   Jump
    +   In Mario's style [(Use broadcast)](https://scratch.mit.edu/projects/115999666/)

### Stories (Unit 3)

+   [Debug it!](https://scratch.mit.edu/studios/475554/)
    +   [Debug 3.1](https://scratch.mit.edu/projects/24269007/): Scratch Cat 教 Gobo 喵喵叫，可是輪到 Gobo 練習時，他沒有喵喵叫，該怎麼辦？
    +   [Debug 3.2](https://scratch.mit.edu/projects/24269046/): 想要設計成輸入一個數字讓 Scratch Cat 數，但他現在每次都是數到 10 ，該怎麼辦？ 
    +   [Debug 3.3](https://scratch.mit.edu/projects/24269070/): Scratch Cat 想要一個一個打電話給朋友，可是按下綠旗後就立刻結束了，該怎麼辦？
    +   [Debug 3.4](https://scratch.mit.edu/projects/24269097/): Scratch Cat 喊 Jump 的時候， Gobo 應該要跳動，但是沒有，該怎麼辦？
    +   [Debug 3.5](https://scratch.mit.edu/projects/24269131/): 恐龍應該只在禮堂跳舞，可是現在恐龍出現在所有場景，並且不會動，該怎麼辦？

### Modularization and Recursion

+   How to draw a tree?
    +   Draw a trunk, then a crown
        +   [Example 1](https://scratch.mit.edu/projects/115904117/)
        +   [Example 2](https://scratch.mit.edu/projects/115903979/)
        +   [Example 3](https://scratch.mit.edu/projects/115848139/)
    +   Draw a crown, then several branches, then a trunk.
        +   [Example](https://scratch.mit.edu/projects/115838437/)
+   Modularization
    +   Decompose the task into subtasks
        +   More readable
        +   Reusable
+   State
    +   Variable
    +   List
+   Precondition
+   Postcondition
    +   Effect
    +   Side Effect
+   Design Goal
    +   If the precondition is true, then we will have the postcondition after executing the command.
+   Loop Invariants
    +   Example: [Insertion sort](https://scratch.mit.edu/projects/116187770/)
+   Recursion
    +   A block contains itself
    +   Infinite loop and recursive calls without terminal condition
    +   Expansion
    +   Draw a tree recursively
        +   Try to search tree [here](https://scratch.mit.edu/).
        +   [Example 1](https://scratch.mit.edu/projects/115835376/)
        +   [Example 2](https://scratch.mit.edu/projects/115837227/)
        +   [Example 3](https://scratch.mit.edu/projects/115840771/)
        +   [Example 4](https://scratch.mit.edu/projects/115688213/)
        +   [Magically non-recursive tree](https://scratch.mit.edu/projects/115834535/)
+   Task
    +   Draw a snowflake
    +   Optional: [Draw a Koch snowflake](https://en.wikipedia.org/wiki/Koch_snowflake)

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