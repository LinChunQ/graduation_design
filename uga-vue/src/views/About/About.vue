<script setup>

</script>

<template>
  <div class="about-container">
    <div class="title">关于我们</div>
    <div class="content">
      <!-- 关于说明 -->
      <div class="about-text">
        <p>
          本系统采用Vue3作为前端框架，Flask作为后端框架，MySQL作为数据库，Redis作为验证码缓存，并采用Docker作为容器化技术和Jenkins作为持续集成和持续部署工具，实现系统部署和运维。
        </p>
      </div>
      <!-- 展示图片 -->
      <div class="about-img">
        <div class="img-box">
          <img class="img" src="@/assets/imgs/font.png" alt="关于我们">
          <div class="label">前端技术</div>
        </div>
        <div class="img-box">
          <img class="img" src="@/assets/imgs/backEnd.png" alt="关于我们">
          <div class="label">后端技术</div>
        </div>
        <div class="img-box">
          <img class="img" src="@/assets/imgs/ai.png" alt="关于我们">
          <div class="label">人工智能</div>
        </div>
      </div>
    </div>
    <div class="join-us">
      <el-tooltip effect="light"content="通过该邮箱联系我们：497603213@qq.com" placement="top">
        <div class="label">加入我们</div>
      </el-tooltip>
      <dv-decoration3 style="width:250px;height:30px;"/>
    </div>
  </div>
</template>

<style scoped lang="scss">
.about-container{
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  height: 100%;  /* 使其填满整个屏幕 */
  background-image: url('@/assets/imgs/Home-background1.png'); /* 这里使用你的背景图路径 */
  background-size: cover;  /* 背景图覆盖整个区域 */
  background-position: center;  /* 背景居中 */
  background-repeat: no-repeat;  /* 防止背景重复 */
  overflow: hidden;
}
.title{
    font-size: 25px;
    font-weight: bold;
    color: #fff;
    margin-top: 8%;
  }
.content{
    font-size: 18px;
    color: #fff;
    height: 100%;

    .about-text{
      height: 10%;
    }
    .about-img{
      display: flex;
      justify-content:center;
      align-items: center;
      gap:50px;
      height: 80%;
    }
    .img-box{
      display: flex;
      flex-direction: column;
      align-items: center;
      height: 200px;
      width: 200px;
      font-size: 20px;
      color: #fff;
      .img{
        height: 85%;
        width: 85%;
        border-radius: 50%;
        margin-bottom: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.3);
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

.label{
        font-size:larger;
        font-weight:bolder;
}
</style>