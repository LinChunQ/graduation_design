<script setup>
import { ref, reactive, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import  useAuthStore  from '../stores/useStoreAuth'
import SIdentify from '../components/SIdentify.vue'

const router = useRouter()
const authStore = useAuthStore()
const {handleLogin,isLogin}=authStore
const Role = ref('1')
const identifyCode=ref()
const code=ref('')
// 表单数据
const loginForm = reactive({
  role:Role.value,
  username: '',
  password: ''
})

const errorMsg = ref('')
const isFormValid = ref(false)

// 输入验证
const validateInput = () => {
  // 基本验证
  if (loginForm.username && loginForm.password) {
      isFormValid.value = true
      errorMsg.value = ''
  } else {
      isFormValid.value = false
  }
}

// 登录处理
const login = async () => {
  if(code.value!==identifyCode.value){
    errorMessage('验证码错误');
    return;
  } 
  // 防止XSS攻击
  const xssPattern = /(~|\{|\}|"|'|<|>|\?)/g
  if (xssPattern.test(loginForm.username) || xssPattern.test(loginForm.password)) {
      errorMessage('警告:输入内容包含非法字符');
      return
  }
  try {
      localStorage.setItem('role',Role.value);
      await handleLogin({ username: loginForm.username, password: loginForm.password ,role:Role.value})
      // 跳转到主页
      router.push('/')
  } catch (error) {
      errorMessage('登录失败，请稍后重试');
  }
}

function reset(){
  loginForm.username = ''
  loginForm.password = ''
}
// 错误提示
const errorMessage = (text) => {
  errorMsg.value = text
  setTimeout(() => {
      errorMsg.value = ''
  }, 3000)
}

//随机生成4位验证码
const randomCode = () => {
  return Math.floor(1000 + Math.random() * 9000).toString();
}

const changeCode=()=>{
  identifyCode.value=randomCode()
}

onMounted(() => {
  reset()
  validateInput()
  identifyCode.value=randomCode()
})

onUnmounted(()=>{
  reset()
})


</script>

<template>
  <div class="login-wrapper">
      <div class="login-container">
          <div class="form-header">
              <h2>用户登录</h2>
              <p>欢迎回来，请登录您的账号</p>
          </div>
          <form @submit.prevent="login" class="floating-form">
              <div class="input-group">
                  <input id="username" v-model.trim="loginForm.username" type="text" autocomplete="off" @input="validateInput" required />
                  <label for="username">用户名</label>
                  <span class="highlight"></span>
              </div>
              <div class="input-group">
                  <input id="password" v-model.trim="loginForm.password" type="password" autocomplete="off" @input="validateInput" required />
                  <label for="password">密码</label>
                  <span class="highlight"></span>
              </div>
              <div class="error-message" v-if="errorMsg">{{ errorMsg }}</div>
              <div class="form-middle">
                <el-radio-group v-model="Role">
                  <el-radio :value="'0'">管理员</el-radio>
                  <el-radio :value="'1'">普通用户</el-radio>
                </el-radio-group>
                <el-input v-model="code" style="height:35px; width: 120px;" placeholder="请输入验证码" />
                <SIdentify :identifyCode="identifyCode" @click="changeCode"/>
              </div>
              <button type="submit" class="submit-btn" :disabled="!isFormValid">
                  <span>登录</span>
                  <i class="arrow-icon"></i>
              </button>
              <div class="form-footer">
                
                <div class="forget" v-if="false">
                  <a href="/forget">忘记密码？</a>
                </div>
                <div class="reset"  @click="reset">重置</div>
                <div class="reg">
                  <span>还没有账号？</span>
                  <a href="/register">立即注册</a>
                </div>
                  
              </div>
          </form>
      </div>
  </div>
</template>

<style scoped lang="scss">
.login-wrapper {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  padding: 20px;
}

.login-container {
  width: 100%;
  max-width: 480px;
  background: white;
  border-radius: 20px;
  padding: 0 40px 40px 40px;
  padding-right: 80px;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
}

.form-header {
  text-align: center;
  margin-bottom: 20px;
}

.form-header h2 {
  color: #2c3e50;
  font-size: 32px;
  margin-bottom: 10px;
  font-weight: 700;
}

.form-header p {
  color: #95a5a6;
  font-size: 16px;
}

.floating-form .input-group {
  position: relative;
  margin-bottom: 20px;
}

.input-group input {
  width: 100%;
  padding: 15px;
  border: 2px solid #e0e0e0;
  border-radius: 12px;
  font-size: 16px;
  transition: all 0.3s ease;
  background: transparent;
}

.input-group label {
  position: absolute;
  left: 15px;
  top: 50%;
  transform: translateY(-50%);
  background: white;
  color: #95a5a6;
  font-size: 16px;
  transition: all 0.3s ease;
  pointer-events: none;
}

.input-group input:focus,
.input-group input:valid {
  border-color: #3498db;
}

.input-group input:focus + label,
.input-group input:valid + label {
  top: 0;
  font-size: 14px;
  color: #3498db;
}

.submit-btn {
  width: 100%;
  padding: 15px;
  margin-left: 15px;
  background: linear-gradient(to right, #3498db, #2980b9);
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 18px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
}

.submit-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(52, 152, 219, 0.3);
}

.arrow-icon {
  border: solid white;
  border-width: 0 2px 2px 0;
  display: inline-block;
  padding: 3px;
  transform: rotate(-45deg);
}

.form-footer {
  display:flex;
  justify-content:flex-end;
  align-items:center;
  text-align: center;
  margin-top: 20px;
  color: #95a5a6;
  gap: 10%;
}

.form-footer a {
  color: #3498db;
  text-decoration: none;
  margin-left: 5px;
  font-weight: 600;
}

.form-footer a:hover {
  text-decoration: underline;
}

.error-message {
  color: #f56c6c;
  font-size: 14px;
  text-align: center;
  margin-bottom: 20px;
}

.reset{
  font-size: 16px;
  color: #95a5a6;
  &:active {
    transform: scale(1.2);
    font-weight: bold;
  }
}

.form-middle{
  display: flex; 
  width: 100%;
  margin-left: 10%;
  margin-bottom: 10px;
  gap: 2%;
}
</style>