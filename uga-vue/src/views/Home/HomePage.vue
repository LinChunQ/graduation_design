<script setup>
import Notice from '../../components/notice/Notice.vue'
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
      <div class="box">
        <div class="img-box">
          <img src="@/assets/imgs/homebg1.png"/>
        </div>
        <div class="disc">
          <strong>AI 智能识别试卷，快速录入成绩</strong>
          运用先进的图像识别与人工智能技术，精准识别试卷上的学生作答情况及分数。无需手动逐一录入，大幅节省时间，将原本漫长的成绩录入工作压缩至最短时间，让您从重复劳动中解脱。
        </div>
      </div>
      <div class="box">
        <div class="img-box">
          <img src="@/assets/imgs/homebg2.png"/>
        </div>
        <div class="disc">
          <strong>自动生成成绩报表，多种格式导出</strong>
          系统可根据录入的成绩数据，自动生成清晰、规范的成绩报表。无论是常见的 Excel 格式，还是便于展示的 PDF 格式等，均可一键导出，方便您存档、分析以及向上汇报。
        </div>
      </div>
      <div class="box">
        <div class="img-box">
          <img src="@/assets/imgs/homebg3.png"/>
        </div>
        <div class="disc">
          <strong>智能分析成绩数据，提供教学改进建议</strong>
          借助大数据分析与智能算法，深度剖析成绩数据背后的规律。不仅能呈现班级整体成绩分布、各分数段人数等基础信息，还能通过对比分析、趋势预测等手段，为您提供针对性强、切实可行的教学改进建议，助力教学质量稳步提升。
        </div>
      </div>
    </div>
   
  </div>
</template>

<style scoped lang="scss">
.Container{
  width: 100%;
  height: 100vh;  /* 使其填满整个屏幕 */
  background-image: url('@/assets/imgs/Home-background1.png'); /* 这里使用你的背景图路径 */
  background-size: cover;  /* 背景图覆盖整个区域 */
  background-position: center;  /* 背景居中 */
  background-repeat: no-repeat;  /* 防止背景重复 */
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
  .t2{
    margin-left:35%;
  }
}

.content{
  display:flex;
  justify-content:center;
  height:60%;
  width:100%;
  gap:5%;
  .box{
    margin-top:1%;
    height:100%;
    width:18%;
    border-radius:0px 0px 8px 8px;
    //box-shadow: 1px 1px 4px rgba(255, 255, 255, 0.5);
    .disc{
    margin-top:3%;
    height:40%;
    width:100%;
    color:#fff;
    font-size:17px;
    padding:5px;
  }
  }
  .img-box{
    height:60%;
    width:auto;
    background-size:cover;
  }
  .img-box img {
    width: 100%;
    height: 100%;
  }
  
}

</style>
