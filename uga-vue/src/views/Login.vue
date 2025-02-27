<template>
  <div class="login-container">
    <div class="login-box">
      <h2 class="login-title">用户登录</h2>
      <el-form 
        ref="formRef" 
        :model="form" 
        :rules="rules"
        @keyup.enter="handleLogin"
      >
        <el-form-item prop="username">
          <el-input
            v-model="form.username"
            prefix-icon="User"
            placeholder="请输入账号"
            clearable
          />
        </el-form-item>

        <el-form-item prop="password">
          <el-input
            v-model="form.password"
            prefix-icon="Lock"
            placeholder="请输入密码"
            show-password
            clearable
          />
        </el-form-item>

        <el-form-item class="action-buttons">
          <el-button
            type="primary"
            :loading="loading"
            @click="handleLogin"
          >
            登录
          </el-button>
          <el-button @click="resetForm">
            重置
          </el-button>
          <el-link
            type="primary"
            class="register-link"
            @click="handleRegister"
          >
            立即注册
          </el-link>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { ElMessage } from 'element-plus'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'

const router = useRouter()
const userStore = useUserStore()
const formRef = ref()

// 修改setup部分
const form = reactive({
  username: '',
  password: ''
})

const loading = ref(false)

// 修改验证规则
const rules = {
  username: [
    { required: true, message: '请输入账号', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' }
  ]
}
// 登录处理
const handleLogin = async () => {
  try {
    await formRef.value.validate()
    state.loading = true
    
    // 调用store的登录方法
    await userStore.login({
      username: state.form.username,
      password: state.form.password
    })

    ElMessage.success('登录成功')
    router.push('/')
  } catch (error) {
    if (error?.errorCode) {
      ElMessage.error(error.message || '登录失败')
    }
  } finally {
    state.loading = false
  }
}

// 重置表单
const resetForm = () => {
  formRef.value.resetFields()
}

// 跳转注册
const handleRegister = () => {
  router.push('/register')
}
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(45deg, #f3f4f6, #e5e7eb);
  background-size: cover;
}

.login-box {
  width: 380px;
  padding: 40px;
  background: rgba(255, 255, 255, 0.95);
  border-radius: 8px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.login-title {
  text-align: center;
  margin-bottom: 30px;
  color: #2c3e50;
  font-size: 24px;
  font-weight: 600;
}

.action-buttons {
  display: flex;
  justify-content: space-between;
  margin-top: 30px;
}

.register-link {
  margin-left: auto;
  cursor: pointer;
}

:deep(.el-input__inner) {
  height: 42px;
}
</style>