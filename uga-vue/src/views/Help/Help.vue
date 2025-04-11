<script setup>
const dialogFormVisible = ref(false)
const formLabelWidth = '140px'
const form = reactive({
  name: '',
  region: '',
  date1: '',
  date2: '',
  delivery: false,
  type: [],
  resource: '',
  desc: '',
})

</script>

<template>
  <div class="container">
    <div class="header">
        <div class="title">使 用 指 南</div>
        <div class="feedback" @click="dialogFormVisible = true">
            <img src="../../assets/feedback.avif"/>
        </div>
    </div>
    <div class="content">
        <div class="box">
            <dv-border-box8 :dur="6">
                <img class="box-img" src="@/assets/imgs/introFunc.png" alt="功能介绍"/>
                <div class="box-name">智能批改</div>
            </dv-border-box8>
        </div>
        <div class="box">
            <dv-border-box8 :dur="6">
                <img class="box-img" src="@/assets/imgs/hisFunc.png" alt="功能介绍"/>
                <div class="box-name">历史使用</div>
            </dv-border-box8>
        </div>
        <div class="box">
            <dv-border-box8 :dur="6">
                <img class="box-img" src="@/assets/imgs/statisFunc.png" alt="功能介绍"/>
                <div class="box-name">统计分析</div>
            </dv-border-box8> 
        </div>
        <div class="box">
            <dv-border-box8 :dur="6">
                <img class="box-img" src="@/assets/imgs/reFunc.png" alt="功能介绍"/>
                <div class="box-name">相关文章</div>
            </dv-border-box8>
        </div>
    </div>
    
  </div>

    <!-- 弹窗对话框 -->
  <el-dialog v-model="dialogFormVisible" title="感谢您的反馈!" width="500">
    <el-form :model="form">
        <el-form-item>
            亲爱的用户朋友， 感谢您使用高校教师助手！为了共创更好的平台，我们期待您宝贵的意见和建议：
        </el-form-item>
        <el-form-item label="">
            <el-input v-model="form.desc" type="textarea" :rows="6" />
        </el-form-item>
    </el-form>
    <template #footer>
      <div class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取消</el-button>
        <el-button type="primary" @click="dialogFormVisible = false">
          提交
        </el-button>
      </div>
    </template>
  </el-dialog>
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
    display: flex;
    justify-content:flex-end;
    align-items:center;
    width:100vw;
    padding:20px;
    height: 10vh;
    margin-top: 30px;
    .title{
        margin-top:80px;
        font-size: 48px;
        margin-right:25%;
        font-weight: bold;
        color: rgb(255, 255, 255);
        gap:20px;
        text-align: center;
    }
    .feedback{
        width:70px;
        height:80px;
        margin-top:8%;
        margin-right:15%;
        img{
            width:70px;
            height:80px;
        }
        &:active {
        transform: scale(0.95); // 点击时缩小
    }
    }
}
.content{
    margin-top:30px;
    display:flex;
    width:100vw;
    height: 70vh;
    //border:1px solid rgb(255, 255, 255);
    justify-content: center; // 使内容水平居中
    gap:50px;
}
.box{
    display:flex;
    flex-direction: column;
    align-items: center;
    margin-top:80px;
    height:200px;
    width:200px;
    background-color: #5f89b9;
    box-shadow: 0 0 10px rgba(148, 147, 147, 0.5);
    border-radius: 10px;
    padding: 20px;
    transition: transform 0.2s; // 添加过渡效果
    cursor: pointer; // 改变鼠标指针样式
    &:active {
        transform: scale(0.95); // 点击时缩小
    }
    .box-img{
        margin-top:10px;
        margin-left:20px;
        width:80%;
        height:80%;
        //图片颜色#2a367d
    }
    .box-name{
        font-size: 20px;
        letter-spacing: 3px;
        color: #fff;
        text-align: center;
    }
}
</style>