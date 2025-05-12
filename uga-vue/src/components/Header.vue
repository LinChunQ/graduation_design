<script setup>
import { ElMessageBox } from 'element-plus'
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import useAuthStore from '../stores/useStoreAuth'
import useUserStore from '../stores/useStoreUser'

const router = useRouter()
const authStore = useAuthStore()
const userStore=useUserStore()
const isLoggedIn=ref(false)
const isAdmin=ref(false)
const handleLogout = () => {
  ElMessageBox.confirm('确定要注销当前账号吗？', '注销确认', {
    confirmButtonText: '确定',
    cancelButtonText: '取消',
    type: 'warning'
  }).then(() => {
    authStore.logout()
    isLoggedIn.value=false;
    router.push('/login')
  })
}
onMounted(()=>{
  if(authStore.token){
    userStore.getUserInfo({"role":authStore.role})
    isLoggedIn.value = true;
    if(authStore.role=='0'){
    isAdmin.value=true;
  }else{
    isAdmin.value=false;
  }
  }
})

watch(()=>authStore.isLogin,(newVal)=>{
  isLoggedIn.value=newVal;
  if(authStore.role=='0'){
    isAdmin.value=true;
  }else{
    isAdmin.value=false;
  }
 if(newVal) userStore.getUserInfo({"role":authStore.role})
},{deep:true})

</script>

<template>
  <div class="menu-box">
    <!-- 左侧Logo区 -->
    <div class="menu-logo">
      <img src="@/assets/icons/logo.png" alt="Logo" class="logo-image"/>
      <label class="logo_name">高校教师助手</label>
    </div>
    
    <!-- 中间导航区 -->
    <div class="menun-main">
        <div class="menu-item">
          <el-icon><House /></el-icon>
          <router-link to="/" active-class="active-link">主页</router-link>
        </div>
        <div class="menu-item">
          <el-icon><Monitor /></el-icon>
          <router-link to="/smart-correction" active-class="active-link">智能批改</router-link>
        </div>
        <div class="menu-item">
          <el-icon><Tickets /></el-icon>
          <router-link to="/history" active-class="active-link">历史使用</router-link>
        </div>
        <div class="menu-item">
          <el-icon><PieChart /></el-icon>
          <router-link to="/statistics" active-class="active-link">统计分析</router-link>
        </div>
        <div class="menu-item" v-if="isAdmin">
          <el-icon><Message /></el-icon>
          <router-link to="/feedback" active-class="active-link">反馈管理</router-link>
        </div>
        <div class="menu-item" v-if="isAdmin">
          <el-icon><Notification /></el-icon>
          <router-link to="/notice" active-class="active-link">公告管理</router-link>
        </div>
        <div class="menu-item">
          <el-icon><Service /></el-icon>
          <router-link to="/help" active-class="active-link">帮助</router-link>
        </div>
        <div class="menu-item">
          <el-icon><Promotion /></el-icon>
          <router-link to="/about" active-class="active-link">关于</router-link>
        </div>
      
    </div>

      <!-- 右侧用户区 -->
      <div class="menu-user">
        <div class="menu-item" v-if="isLoggedIn">
          <el-icon><User /></el-icon>
          <router-link to="/user-info" active-class="active-link">{{'个人信息' }}</router-link>
        </div>
        <div class="menu-item">
          <span  v-if="isLoggedIn" @click="handleLogout" class="logout-btn" >
            点击注销
          </span>
          <router-link v-else to="/login" active-class="active-link">请登录</router-link>
        </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.menu-box {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  padding: 10px 5vw;
  background: #043873;
  min-width: 50%;
}
/* 左侧Logo容器 */
.menu-logo {
  display: flex;
  align-items: center;
  flex: 0 0 auto;
  min-width: 5%;
  margin-right: 50px; // 与中间导航保持距离

  .logo_name {
    margin-left: 15px;
    font-size: 20px;
    font-weight: bold;
    letter-spacing: 0.3em;
    color: white;
    text-wrap: nowrap;
  }
    
  .logo-image {
  height: 60px;
  }
}

.menu-item{ //每个菜单项
  
  display: flex;
  align-items: center;
  gap: 8px;
  color: white;
  margin-right: 30px;
  cursor: pointer;
  a{
    color: aliceblue;
    text-wrap: nowrap;
    text-decoration: none;
  }
}

/* 中间导航区 */
.menun-main {
  flex: 1 1 auto;
  display: flex;
  justify-content:flex-start ;
  align-items: center;
  height: 100%;
}

/* 右侧用户区 */
.menu-user {
  flex: 0 0 auto;
  display: flex;
  gap: 30px;
  min-width: 220px;
  justify-content: flex-end;
  .logout-btn{
    text-wrap: nowrap;
  }
}

.active-link {
color: #42b983 !important;
font-weight: bold;
}
</style>