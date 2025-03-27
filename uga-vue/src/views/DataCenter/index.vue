<script setup>
</script>

<template>
  <div class="sta-container">
    <el-menu
    :default-active="activeIndex2"
    class="el-menu-demo"
    mode="horizontal"
    background-color="#043873"
    text-color="#fff"
    active-text-color="#ffd04b"
    @select="handleSelect"
  >
     <!-- 左侧Logo区 -->
     <div class="logo-container">
      <img src="@/assets/icons/logo.png" alt="Logo" class="logo-image"/>
      <label class="logo_name">高校教师助手</label>
    </div>
    <el-menu-item index="1"><el-icon><House /></el-icon>首页</el-menu-item>
    <el-sub-menu index="2">
      <template #title><el-icon><Monitor /></el-icon>智能批改</template>
      <el-menu-item index="2-1">单个批改</el-menu-item>
      <el-menu-item index="2-2">批量批改</el-menu-item>
    </el-sub-menu>
    <el-sub-menu index="3">
      <template #title><el-icon><Tickets /></el-icon>历史记录</template>
      <el-menu-item index="3-1">班级</el-menu-item>
      <el-menu-item index="3-2">学校</el-menu-item>
    </el-sub-menu>
    <el-sub-menu index="4">
      <template #title><el-icon><PieChart /></el-icon>数据统计</template>
      <el-menu-item index="4-1">班级</el-menu-item>
      <el-menu-item index="4-2">学校</el-menu-item>
    </el-sub-menu>
    <el-menu-item index="6"><el-icon><Service /></el-icon>帮助</el-menu-item>
    <el-menu-item index="7"><el-icon><Promotion /></el-icon>关于</el-menu-item>
    <!-- 右对齐容器 -->
    <div class="right-align-container">
        <el-menu-item index="8"><el-icon><User /></el-icon>个人信息</el-menu-item>
        <el-menu-item index="9">注销</el-menu-item>
        <el-menu-item index="10" v-show="false">登陆</el-menu-item>
    </div>
  </el-menu>
  </div>
</template>

<style scoped lang="scss">
 .sta-container{
  width:100%;
 }
.el-menu-demo{
  display:flex;
  width:100%;
 
}
/* 左侧Logo容器 */
.logo-container {
    display: flex;
    align-items: center;
    min-width: 280px;
    margin-right: 50px; // 与中间导航保持距离
    
    .logo_name {
      margin-left: 15px;
      font-size: 20px;
      font-weight: bold;
      letter-spacing: 0.3em;
      color: white;
    }
    
    .logo-image {
      height: 60px;
    }
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