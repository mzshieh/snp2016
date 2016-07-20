## Lecture 5

### Review

+   Precondition and postcondition
    +   理解指令的前提與效果
    +   滿足前提就能達到效果
    +   初始化
    +   留意副作用

+   Decomposition
    +   Divide and conquer
        +   大事化小事
            +   先把一件複雜的事情拆解成幾小塊。
            +   還是太大就繼續拆下去。
        +   小事化無事
            +   無事：指令有支援，直接拿來用，就不用自己設計了。
    +   Incremental
        +   千里之行，始於足下。
        +   逐漸改善，累積成效。
        +   設計 Loop invariants 來確保進度。

+   請分享雪花作業成果。

+   [Maze](https://scratch.mit.edu/projects/11414041/)
    +   透過切換背景 (backdrop) 來切換關卡。
+   [Pong](https://scratch.mit.edu/projects/10128515/)
    +   視力測驗：請確定 Color picker 沒有挑錯顏色。
+   [Scrolling](https://scratch.mit.edu/projects/22162012/)
    +   改使用速度來修改座標。改使用固定加速度。而按下空白鍵時，改為修改速度。
+   [Fish Chomp](https://scratch.mit.edu/projects/10859244/)
    +   用個變數記錄分數，並搭配適當的事件修改變數值。
+   [ScratchX](http://scratchx.org/)
    +   eXperimental eXtension
    +   以 JavaScript 開發擴充功能
    +   可能有安全性風險
    +   沒有雲端存檔功能，請記得存檔。

### Game

+   Puzzles 請準備幾個角色
    +   P1: 當你按下 B 時，角色變大一點。當你按下 S 時，角色變小一點。
    +   P2: 當角色透過網路攝影機看到的畫面變化很大時，換個顏色。
    +   P3: 當角色移動到畫面上方 25% 的區域，會說他喜歡上面。
    +   P4: 當角色碰到藍色時，發出一個高音。當角色碰到紅色時，發出一個低音。
    +   P5: 當角色碰到另外一個角色時，其中一個說「不好意思」。
    +   P6: 當貓角色靠近狗角色時，狗跑離貓。
    +   P7: 當滑鼠點擊一下時，在那邊畫朵花。
    +   P8: 當你點擊一個角色時，其他的角色就跳舞。
    +   P9: 當你移動滑鼠時，角色追著滑鼠跑，但不可以碰到滑鼠。
+   [Debug It!](https://scratch.mit.edu/studios/475634/)
    +   [Debug 4.1](https://scratch.mit.edu/projects/24271192/): Scratch Cat 只能撿起筆記型電腦到 Inventory ，請修改程式讓他可以撿起其他東西。
    +   [Debug 4.2](https://scratch.mit.edu/projects/24271303/): 請改到讓 Scratch Cat 碰到黃色 Gobo 時加 10 分，碰到粉紅 Gobo 時減 10 分。
    +   [Debug 4.3](https://scratch.mit.edu/projects/24271446/): 請修好這個猜數字遊戲，讓 Scratch Cat 不要在那邊胡說八道。
    +   [Debug 4.4](https://scratch.mit.edu/projects/24271475/): 請讓球打到 Scratch Cat 一次時，# of hits 只增加 1。
        +   額外要求：讓畫面上有 10 顆球在飛。
        +   Hint: Clone, 分身。
    +   [Debug 4.5](https://scratch.mit.edu/projects/24271560/): 請修改成不會穿過綠色怪物的版本。
