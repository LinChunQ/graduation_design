<script setup>
import Notice from '../../components/notice/Notice.vue'
import BG from './WebGL.vue'
</script>
<template>
  <div class="Container">
      <div class="notice">
       <Notice/>
      </div>
      <div class="title">
        <h1 class="t1">高校教师专属 AI 助手，一键精准统计分数</h1>
        <h2 class="t2">------告别繁琐分数统计，开启智能教学新时代</h2>
      </div>
    <div class="content">
      <BG></BG>
    </div>
  </div>
</template>

<style scoped lang="scss">
.Container{
  width: 100%;
  height: 100%;  /* 使其填满整个屏幕 */
  background-size: cover;  /* 背景图覆盖整个区域 */
  background-position: center;  /* 背景居中 */
  background-repeat: no-repeat;  /* 防止背景重复 */
  pointer-events: none;
}
.notice{
  display:flex;
  justify-content:center;
  height:5%;
  width:100%;
}
.title{
  display:flex;
  flex-direction:column;
  align-items:center;
  height:25%;
  width:100%;
  //border:1px solid #fff;
  color:#fff;
  .t1{
      z-index: 1;
  }
  .t2{
    margin-left:35%;
    z-index: 1;
  }
}

.content{
  // display:flex;
  // justify-content:center;
  height:60%;
  width:100%;
}

</style>
