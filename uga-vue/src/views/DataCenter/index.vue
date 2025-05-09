<script setup>
</script>

<template>
    <el-menu
    :default-active="activeIndex2"
    class="el-menu-demo"
    mode="horizontal"
    background-color="#043873"
    text-color="#fff"
    active-text-color="#81e66c"
    @select="handleSelect"
  >
      <!-- 左侧Logo区 -->
      <div class="logo-container">
        <img src="@/assets/icons/logo.png" alt="Logo" class="logo-image"/>
        <label class="logo_name">高校教师助手</label>
      </div>
      <el-menu-item index="1"><el-icon><House /></el-icon>首页</el-menu-item>
      <el-menu-item index="2"><el-icon><Monitor /></el-icon>智能批改</el-menu-item>
      <el-menu-item index="3"><el-icon><Tickets /></el-icon>历史记录</el-menu-item>
      <el-menu-item index="4"><el-icon><PieChart /></el-icon>数据统计</el-menu-item>
      <el-menu-item index="6"><el-icon><Service /></el-icon>帮助</el-menu-item>
      <el-menu-item index="7"><el-icon><Promotion /></el-icon>关于</el-menu-item>
      <!-- 右对齐容器 -->
      <div class="right-align-container">
          <el-menu-item index="8"><el-icon><User /></el-icon>个人信息</el-menu-item>
          <el-menu-item index="9">点击注销</el-menu-item>
          <el-menu-item index="10" v-show="false">登陆</el-menu-item>
      </div>
  </el-menu>
</template>

<style scoped lang="scss">
.el-menu-demo{
  display:flex;
  justify-content: flex-start;
  align-items: center;
  width:100%;
  padding-left: 5%;
}

.logo_name {
  margin-left: 15px;
  font-size: 20px;
  font-weight: bold;
  letter-spacing: 0.3em;
  color: white;
}
    
.logo-image {
  height: 60px;
  margin-bottom: 15px;
}
  

.right-align-container {
  margin-left:30%;
  display: flex;
  justify-content: flex-end; /* 右对齐 */
}

::v-deep .el-menu-item, ::v-deep .el-sub-menu .el-sub-menu__title {
  font-size: 16px !important; /* 设置字体大小 */
}
</style>