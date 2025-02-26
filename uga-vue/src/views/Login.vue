<template>
    <div class="login-container">
      <div style="width: 350px" class="login-box">
        <div style="front-weight:bold;front-size:24px; text-align:center; margin-bottom: 30px">登录</div>
        <el-form ref="formRef" :model="data.form">
          <el-form-item prop="username">
            <el-input prefix-icon="User" v-model="data.form.username" placeholder="输入账号" />
          </el-form-item>
          <el-form-item prop="password">
            <el-input show-password prefix-icon="Lock" v-model="data.form.password" placeholder="输入密码"/>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click.native="handleLogin">登 录</el-button>
            <el-button type="info" style="margin-left: 50px; " @click.native="resetForm">重置</el-button>
            <el-button type="" style="margin-left: 230px; margin-top: -35px"  @click.native="handleRegister">注册</el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>
</template>

<script setup>
import {reactive ,ref} from "vue";
import {ElMessage} from "element-plus";
import axios from "axios";
import { useRouter } from 'vue-router';
const router = useRouter();
const data=reactive({
  form:{
  },
})
const user= reactive({
  username:[
    { required: true, message: '请输入账号', trigger: 'blur' },
  ],
  password:[
    { required: true, message: '请输入密码', trigger: 'blur' },
  ],
})

const formRef=ref()
const handleLogin = () => {

}
const resetForm=()=>{
  formRef.value.resetFields();   // 表单重置
}
const handleRegister=()=>{
  index.push('/register')
}

</script>

<style scoped>
.login-container{
  min-height:  100vh;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  background-image: url("@/assets/imgs/bg1.jpg");
  background-size: cover;
}
.login-box{
  background-color:rgba(255,255,255,0.85);
  box-shadow: 0 0 10px rgba(0,0,0.1);
  border: 1px solid #addd;
  padding: 30px;
  -webkit-user-select:none;
}
.login_Button{
  -webkit-user-select: auto; /* Safari */
  user-select: none;
}
</style>