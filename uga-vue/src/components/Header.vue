<template>
  <header class="header">
    <div class="logo">
      <!-- 这里可以使用图片或文字作为 Logo -->
      <img src="@/assets/icons/logo.png" alt="Logo" class="logo-image"/>
      <label class="logo_name">高校教师助手</label>
    </div>
    <nav class="nav-links">
      <ul>
        <el-icon size="18px"><House /></el-icon>
        <li><router-link to="/" >主页</router-link></li>
        <el-icon size="18px"><Monitor /></el-icon>
        <li><router-link to="/smart-correction">智能批改</router-link></li>
        <el-icon size="18px"><Tickets /></el-icon>
        <li><router-link to="/history">历史使用</router-link></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
          <el-icon size="18px"><User /></el-icon>
          <li><router-link to="/user-info" >个人信息</router-link></li>
        <li><router-link to="/login" >登录/注册</router-link></li>
      </ul>
    </nav>
  </header>
</template>

<script setup>

// 这里可以选择添加脚本逻辑
</script>

<style scoped>
/* Header 的外部样式 */
.header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background-color: #043873;
  color: white;
  padding: 10px 20px;
  z-index: 10;
  display: flex;
  justify-content: space-between; /* 分配空间，左右对齐 */
  align-items: center; /* 垂直居中 */
}

.logo {
  display: flex;
  align-items: center;
  .logo_name{
    //margin-bottom: -15px;
    margin-left: 10px;
    font-size: 20px;
    font-weight: bold;
    letter-spacing: 0.3em;
  }
}

.logo-image {
  height: 60px; /* 调整 Logo 大小 */
  margin-left: 120px;
}

.nav-links ul {
  display: flex;  /* 使用 Flexbox 布局 */
  list-style: none;
  padding: 0;
  margin: 0;
  transform: translateX(30px); /* 将整个 ul 向左移动 300px */
}

.nav-links ul li {
  margin-left:5px;  /* 每个 li 之间的间距 */
  margin-right: 50px;
}

.nav-links ul li a {
  color: white;
  text-decoration: none;
  font-size: 18px;
  text-align: left;
}

.nav-links ul li a:hover {
  text-decoration: underline;
}
</style>
