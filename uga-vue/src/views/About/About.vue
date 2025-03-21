<script setup>

</script>

<template>
  <div class="container">
    <div class="title">关于我们</div>
    <div class="content">
      <!-- 关于说明 -->
      <div class="about-text">
        <p>
          本系统采用Vue.js作为前端框架，Python作为后端框架，MySQL作为数据库，并采用Docker作为容器化技术，实现系统部署和运维。
        </p>
      </div>
      <!-- 展示图片 -->
      <div class="about-img">
        <div class="img-box">
          <img class="img" src="@/assets/imgs/avatar.jpeg" alt="关于我们">
          <div>图1</div>
        </div>
        <div class="img-box">
          <img class="img" src="@/assets/imgs/avatar.jpeg" alt="关于我们">
          <div>图2</div>
        </div>
        <div class="img-box">
          <img class="img" src="@/assets/imgs/avatar.jpeg" alt="关于我们">
          <div>图3</div>
        </div>
      </div>
    </div>
    <div class="join-us">
      <div >加入我们</div>
      <dv-decoration3 style="width:250px;height:30px;"/>
    </div>
  </div>
</template>

<style scoped lang="scss">
.container{
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100vw;
  height: 100vh;  /* 使其填满整个屏幕 */
  background-image: url('@/assets/imgs/Home-background1.png'); /* 这里使用你的背景图路径 */
  background-size: cover;  /* 背景图覆盖整个区域 */
  background-position: center;  /* 背景居中 */
  background-repeat: no-repeat;  /* 防止背景重复 */

  .title{
    font-size: 25px;
    font-weight: bold;
    color: #fff;
    margin-top: 8%;
    margin-bottom: 20px;
  }
  .content{
    font-size: 18px;
    color: #fff;
    height: 40%;

    .about-text{
      height: 30%;
    }
    .about-img{
      display: flex;
      justify-content:center;
      align-items: center;
      gap:50px;
      height: 60%;
    }
    .img-box{
      display: flex;
      flex-direction: column;
      align-items: center;
      height: 200px;
      width: 200px;
      font-size: 20px;
      color: #fff;
      img{
        height: 80%;
        width: 80%;
        border-radius: 50%;
        margin-bottom: 10px;
      }
    }
  }
  .join-us{
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 5%;
    font-size: 18px;
    color: #fff;
    letter-spacing: 3px;
  }
}
</style>