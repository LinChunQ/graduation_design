<script setup>
</script>

<template>
  <div class="container">
    <div class="header">
        <div class="title">使 用 指 南</div>
    </div>
    <div class="content">
        <div class="box">
            <img class="box-img" src="@/assets/imgs/introducefunction.png" alt="功能介绍"/>
        </div>
        <div class="box">
        </div>
        <div class="box">
        </div>
        <div class="box">
        </div>
    </div>
    
  </div>
</template>

<style scoped lang="scss">
.container{
  display: flex;
  flex-direction: column; //竖直布局
  width: 100%;
  height: 100vh;  /* 使其填满整个屏幕 */
  background-image: url('@/assets/imgs/Home-background1.png'); /* 这里使用你的背景图路径 */
  background-size: cover;  /* 背景图覆盖整个区域 */
  background-position: center;  /* 背景居中 */
  background-repeat: no-repeat;  /* 防止背景重复 */
}
.header{
    width:100vw;
    padding:20px;
    height: 10vh;
    //border:1px solid rgb(255, 255, 255);
    .title{
        margin-top:80px;
        font-size: 26px;
        color: rgb(255, 255, 255);
        gap:20px;
        text-align: center;
    }
}
.content{
    display:flex;
    width:100vw;
    height: 70vh;
    //border:1px solid rgb(255, 255, 255);
    justify-content: center; // 使内容水平居中
    gap:50px;
}
.box{
    margin-top:80px;
    height:200px;
    width:200px;
    background-color: rgb(255, 255, 255);
    box-shadow: 0 0 10px rgba(148, 147, 147, 0.5);
    border-radius: 10px;
    padding: 20px;
    transition: transform 0.2s; // 添加过渡效果
    cursor: pointer; // 改变鼠标指针样式
    &:active {
        transform: scale(0.95); // 点击时缩小
    }
    .box-img{
        width:100%;
        height:100%;
    }
}
</style>