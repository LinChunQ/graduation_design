<script setup>
import { ElMessageBox } from 'element-plus'
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import useAuthStore from '../stores/useStoreAuth'
const router = useRouter()
const authStore = useAuthStore()
const {logout,token,isLogin}=authStore
const isLoggedIn=ref(isLogin)
const handleLogout = () => {
  ElMessageBox.confirm('确定要注销当前账号吗？', '注销确认', {
    confirmButtonText: '确定',
    cancelButtonText: '取消',
    type: 'warning'
  }).then(() => {
    logout()
    isLoggedIn.value=false;
    router.push('/login')
  })
}
onMounted(()=>{
  if(token.value!==null){
    isLoggedIn.value=true;
  }else{
    isLoggedIn.value=false
  }
})
</script>

<template>
  <header class="header">
    <!-- 左侧Logo区 -->
    <div class="logo-container">
      <img src="@/assets/icons/logo.png" alt="Logo" class="logo-image"/>
      <label class="logo_name">高校教师助手</label>
    </div>
    
    <!-- 中间导航区 -->
    <nav class="main-nav">
      <ul>
        <li class="nav-item">
          <el-icon><House /></el-icon>
          <router-link to="/">主页</router-link>
        </li>
        <li class="nav-item">
          <el-icon><Monitor /></el-icon>
          <router-link to="/smart-correction">智能批改</router-link>
        </li>
        <li class="nav-item">
          <el-icon><Tickets /></el-icon>
          <router-link to="/history">历史使用</router-link>
        </li>
        <li class="nav-item">
          <el-icon><PieChart /></el-icon>
          <router-link to="/statistics">统计分析</router-link>
        </li>
        <li class="nav-item">
          <el-icon><Service /></el-icon>
          <router-link to="/help">帮助</router-link>
        </li>
        <li class="nav-item">
          <el-icon><Promotion /></el-icon>
          <router-link to="/about">关于</router-link>
        </li>
      </ul>
    </nav>

      <!-- 右侧用户区 -->
      <div class="user-nav">
      <div class="nav-item" v-if="isLoggedIn">
        <el-icon><User /></el-icon>
        <router-link to="/user-info">{{'个人信息' }}</router-link>
      </div>
      <div class="nav-item">
        <span v-if="isLoggedIn" @click="handleLogout" class="logout-btn">
          点击注销
        </span>
        <router-link v-else to="/login">请登录</router-link>
      </div>
    </div>
  </header>
</template>

<style lang="scss" scoped>
.header {
  display: flex;
  align-items: center;
  padding: 10px 5vw;
  background: #043873;

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

  /* 中间导航区 */
  .main-nav {
    flex: 1;
    ul {
      display: flex;
      gap: 40px;
      margin: 0;
      padding: 0;
      list-style: none;
      li {
        color: white;
        &:last-child::after {
          content: none;
        }
      }
      .el-icon {
        top: 2px; // 微调图标位置
        margin-right: 6px;
      }
    }
  }

  /* 右侧用户区 */
  .user-nav {
    display: flex;
    gap: 30px;
    min-width: 220px;
    justify-content: flex-end;
    
    .nav-item {
      color: white;
      display: flex;
      align-items: center;
      gap: 8px;
    }
  }

  /* 通用样式 */
  a {
    color: white;
    text-decoration: none;
    font-size: 16px;
    &:hover {
      text-decoration: underline;
    }
  }

  /* 断点1：900px屏幕 */
  @media (max-width: 900px) {
    padding: 10px 3vw;
    
    .logo-container {
      min-width: 200px;
      margin-right: 30px;
      
      .logo-image {
        height: 50px;
      }
      
      .logo_name {
        font-size: 18px;
      }
    }
    
    .main-nav ul {
      gap: 25px;
    }
    
    .user-nav {
      gap: 20px;
      min-width: 180px;
    }
  }

  /* 断点2：700px屏幕 */
  @media (max-width: 700px) {
    flex-wrap: wrap;
    
    .logo-container {
      margin-right: 0;
      margin-bottom: 10px;
      width: 100%;
      justify-content: center;
    }
    
    .main-nav {
      order: 3;
      width: 100%;
      margin-top: 10px;
      
      ul {
        justify-content: center;
        gap: 15px;
      }
    }
    
    .user-nav {
      min-width: auto;
      margin-left: auto;
    }
  }

  /* 断点3：500px屏幕 */
  @media (max-width: 500px) {
    .main-nav ul {
      flex-wrap: wrap;
      justify-content: center;
      gap: 10px 20px;
    }
    
    .user-nav {
      gap: 15px;
      
      a {
        font-size: 14px;
      }
    }
  }
  
  /* 新增的注销按钮样式 */
  .user-nav {
    .logout-btn {
      cursor: pointer;
      color: white;
      &:hover {
        text-decoration: underline;
      }
    }
    
    .nav-item:last-child {
      margin-left: 15px;
    }
  }
}
</style>