## Lecture 3

### Review

+   [Slide (PDF)](snp_lec03.pdf)
+   [Slide (PowerPoint)](snp_lec03.pptx)
+   [Debug it!](http://scratch.mit.edu/studios/475483): [Instructor's solution](https://scratch.mit.edu/studios/2923436/)
    +   [Debug 1.1](https://scratch.mit.edu/projects/10437040/): 希望點下綠旗後，兩隻都在跳舞。可是現在的程式只有一隻會跳，該怎麼辦？
    +   [Debug 1.2](https://scratch.mit.edu/projects/10437249/): 希望按下綠旗後，貓咪能從舞台左邊走到右邊。可是按下去第一次會動，第二次以後就不會動了，該怎麼辦？
    +   [Debug 1.3](https://scratch.mit.edu/projects/10437366/): 希望空白鍵按下後貓咪能夠翻轉一圈。可是怎麼按貓咪就是不動，該怎麼辦？
    +   [Debug 1.4](https://scratch.mit.edu/projects/10437439/): 希望貓咪左右來回移動，可是他碰到邊緣後卻變得頭下腳上，該怎麼辦？
    +   [Debug 1.5](https://scratch.mit.edu/projects/10437476/): 希望按下去後貓咪能夠喵喵喵叫三聲：發出聲音跟顯示出對話框。可是他只叫一聲，而且對話泡泡顯示的方式不對。

### Animation

+   [Build-A-Band](https://scratch.mit.edu/projects/115908616/)
    +   [The official studio](https://scratch.mit.edu/studios/475523/)
    +   Loop
    +   Event
    +   Sound
        +   Drum and instructment
    +   Parallelism
        +   Oberservation: "When key pressed" versus "When this sprite clicked"
            +   See this [project](https://scratch.mit.edu/projects/115950064/)
            +   Race condition
+   [Orange Square, Purple Circle](https://scratch.mit.edu/projects/115908969/)
    +   [The official studio](https://scratch.mit.edu/studios/475527/)
    +   `bitmap` versus `vector`
    +   Sprite versus costume
    +   Effects
+   [It's Alive](https://scratch.mit.edu/projects/115909525/)
    +   [The official studio](https://scratch.mit.edu/studios/475529/)
    +   Broadcast
+   [Music Video](https://scratch.mit.edu/projects/115909681/)
    +   [The official studio](https://scratch.mit.edu/studios/475517/)
+   [Debug it!](https://scratch.mit.edu/studios/475539/)
    +   [Debug 2.1](https://scratch.mit.edu/projects/23266426/): 希望按下 Scratch Cat 後他會隨鼓聲跳舞，但他沒跳，該怎麼辦？
    +   [Debug 2.2](https://scratch.mit.edu/projects/24268476/): 希望 Nano 被碰到的時候也要說話，該怎麼辦？
    +   [Debug 2.3](https://scratch.mit.edu/projects/24268506/): 希望畫個笑臉，目前有一些地方多畫了，該怎麼辦？
    +   [Debug 2.4](https://scratch.mit.edu/projects/23267140/): 希望花開完了要停下來，該怎麼辦？
    +   [Debug 2.5](https://scratch.mit.edu/projects/23267245/): 希望生日快樂歌唱完才提示可以吹蠟燭了。

### Stories

+   [Characters](https://scratch.mit.edu/projects/115946864/)
    +   Implement small jumps, big jumps, and custom jumps
+   [Conversation](https://scratch.mit.edu/projects/10015800/)
    +   Modification: Use broadcast to trigger the conversation
+   [Scene](https://scratch.mit.edu/projects/115947152/)
    +   Press the left arrow to move to the left
    +   Press the right arrow to move to the right
    +   Press the space bar to jump
    +   Modify this project to make Scratch Cat jumping in Mario's style
        +   [Reference](https://wiki.scratch.mit.edu/wiki/When_()_Key_Pressed_(block))
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
+   Loop Invariants
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