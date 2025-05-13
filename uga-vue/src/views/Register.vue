<template>
  <div class="register-wrapper">
      <div class="register-container">
          <div class="form-header">
              <h2>创建账号</h2>
              <p>开启您的美好旅程</p>
          </div>
          <form @submit.prevent="register" class="floating-form">
              <div class="input-group">
                  <input type="text" id="username" v-model="userInfo.username" required maxlength="20" />
                  <label for="username">用户名</label>
                  <span class="highlight"></span>
              </div>
              <div class="input-group">
                  <input type="text" id="sex" v-model="userInfo.sex" required maxlength="20" />
                  <label for="sex">性别</label>
                  <span class="highlight"></span>
              </div>
              <div class="input-group">
                  <input type="tel" id="phone" v-model="userInfo.phone" required maxlength="20" />
                  <label for="phone">手机号</label>
                  <span class="highlight"></span>
              </div>
              <div class="input-group">
                  <input type="text" id="profession" v-model="userInfo.profession" required />
                  <label for="profession">专业名称</label>
                  <span class="highlight"></span>
              </div>
              <div class="input-group">
                  <input type="text" id="school" v-model="userInfo.school" required />
                  <label for="school">学校</label>
                  <span class="highlight"></span>
              </div>
              <div class="input-group">
                  <input type="email" id="email" v-model="userInfo.email" required />
                  <label for="email">邮箱</label>
                  <span class="highlight"></span>
              </div>
              <div class="input-group verification-group">
                  <input type="text" id="verificationCode" v-model="userInfo.captcha" required maxlength="6" />
                  <label for="verificationCode">验证码</label>
                  <button type="button" @click="sendVerificationCode" class="send-code-btn">{{captchaText}}</button>
                  <span class="highlight"></span>
              </div>
              <div class="input-group">
                  <input type="password" id="password" v-model="userInfo.password" required minlength="5" maxlength="20" />
                  <label for="password">密码</label>
                  <span class="highlight"></span>
              </div>
              <div class="input-group">
                  <input type="password" id="confirmPassword" v-model="confirmPassword" required minlength="5" maxlength="20" />
                  <label for="confirmPassword">确认密码</label>
                  <span class="highlight"></span>
              </div>
              <button type="submit" class="submit-btn">
                  <span>立即注册</span>
                  <i class="arrow-icon"></i>
              </button>
              <div class="footer">  
                <div class="reset"  @click="reset">重置</div>
                <div class="form-footer">
                  <span>已有账号？</span>
                  <a href="/login">立即登录</a>
              </div>
              </div>
              
          </form>
      </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import useAuthStore from "../stores/useStoreAuth.js";
import {useRouter} from 'vue-router'
import {ElMessage} from "element-plus";
import {getCaptcha} from '../apis/auth'
const authStore=useAuthStore();
const router=useRouter()
const {handleRegister}=authStore
const userInfo=reactive({
  username:'',
  sex:'',
  phone:'',
  email:'',
  profession:'',
  school:'',
  password:'',
  captcha:''
})

const verificationCode = ref('')
const confirmPassword = ref('')

const totalTime = ref(60)//倒计时
const captchaText=ref('获取验证码')
const isClick=ref(true) //控制按钮是否可用
async function register (){
  if(userInfo.password!==confirmPassword.value){
    ElMessage.error("两次密码不相等!");
  }

  await  handleRegister(userInfo)
  router.push('/login')
}

const sendVerificationCode = async () => {
  if(!isClick.value) return;
  else isClick.value=false;

  let clock = window.setInterval(() => {
  captchaText.value =totalTime.value + 's后重新发送'
  totalTime.value--
  if (totalTime.value < 0) {     //当倒计时小于0时清除定时器
    window.clearInterval(clock)
    captchaText.value = '重新发送验证码'
    totalTime.value = 60;
    isClick.value=true;
    }
  },1000)
  await getCaptcha({email: email.value});
}

const reset=()=>{
  userInfo.username=''
  userInfo.sex=''
  userInfo.phone=''
  userInfo.email=''
  userInfo.profession=''
  userInfo.school=''
  userInfo.password=''
  confirmPassword.value=''
  verificationCode.value=''
}

onMounted(()=>{
  
})
</script>

<style scoped lang="scss">
.register-wrapper {
  height: 100%;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

.register-container {
  width: 100%;
  max-width: 480px;
  background: white;
  border-radius: 20px;
  padding: 0 30px 0 30px;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
  margin-top: 30px;
}

.form-header {
  text-align: center;
}

.form-header h2 {
  color: #2c3e50;
  font-size: 32px;
 // margin-bottom: 10px;
  font-weight: 700;
  margin-bottom: 0;
}

.form-header p {
  color: #95a5a6;
  font-size: 16px;
  margin: 8px;
}

.floating-form .input-group {
  position: relative;
  margin-bottom: 15px;
}

.input-group input {
  width: 95%;
  padding: 10px;
  border: 2px solid #e0e0e0;
  border-radius: 12px;
  font-size: 14px;
  transition: all 0.3s ease;
  background: transparent;
}

.input-group label {
  position: absolute;
  left: 15px;
  top: 50%;
  transform: translateY(-50%);
  background: #fff;
  padding: 0;
  color: #95a5a6;
  font-size: 14px;
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
  font-size: 12px;
  color: #3498db;
}

.verification-group {
  display: flex;
  gap: 10px;
}

.verification-group input {
  flex: 1;
}

.send-code-btn {
  padding: 0 20px;
  background: #e8f5fe;
  color: #3498db;
  border: none;
  border-radius: 12px;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.3s ease;
  white-space: nowrap;
}

.send-code-btn:hover {
  background: #d0e9fd;
}

.submit-btn {
  width: 100%;
  padding: 15px;
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

.footer{
  display: flex;
  justify-content: flex-start; 
  align-items: center;
  gap: 25%;
  padding: 10px;
  .reset{
  margin-top: 15px;
  font-size: 16px;
  color: #95a5a6;
  &:active {
    transform: scale(1.2);
    font-weight: bold;
  }
}
}

.form-footer {
  text-align: center;
  margin-top: 20px;
  color: #95a5a6;
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
</style>