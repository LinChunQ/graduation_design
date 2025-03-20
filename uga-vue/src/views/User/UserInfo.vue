<script setup>
import { ref, onMounted, reactive } from 'vue';
import userAvatar from '@/assets/imgs/avatar.jpeg'
import  useAuthStore  from '../../stores/useStoreAuth'
const authStore = useAuthStore()
const {userInfo}=authStore
const formSize = ref('default') 
const ruleFormRef = reactive(userInfo)
const ruleForm = reactive(userInfo)

const rules = reactive({
  name: [
    { required: true, message: '请输入姓名!', trigger: 'blur' },
    { min: 2, max: 15, message: '姓名长度2~15个!', trigger: 'blur' },
  ],
  sex: [
    {
      required: true,
      message: '请选择性别!',
      trigger: 'change',
    },
  ],
  school: [
    { required: true, message: '请输入学校!', trigger: 'blur' },
    { min: 2, max: 25, message: '学校名称长度2~25个!', trigger: 'blur' },
  ],
  profession: [
    { required: true, message: '请输入专业!', trigger: 'blur' },
    { min: 2, max: 25, message: '专业名称长度2~25个!', trigger: 'blur' },
  ],
  phone: [
    { required: true, message: '请输入手机号!', trigger: 'blur' },
    { min: 11, max: 11, message: '手机号长度必须为11位!', trigger: 'blur' },
  ],
  desc: [
    { required: true, message: 'Please input activity form', trigger: 'blur' },
  ],
})

const submitForm = async (formEl) => { 
  if (!formEl) return
  await formEl.validate((valid, fields) => {
    if (valid) {
      console.log('submit!')
    } else {
      console.log('error submit!', fields)
    }
  })
}

const resetForm = (formEl) => { 
  if (!formEl) return
  formEl.resetFields()
}

onMounted(() => {
  debugger
  console.log(ruleForm)
})

watch(userInfo,(newVal)=>{
  debugger
  Object.assign(ruleForm,newVal)
})
</script>

<template>
  <div class="conatainer">
    <!-- 侧边栏 -->
    <div class="userInfo">
      <el-image class="avatar" :src="userAvatar" />
      <el-form :model="ruleForm" label-width="auto" style="max-width: 350px; margin-top:50px; margin-right: 35px">
        <el-form-item label="姓名:">
          <el-input v-model="ruleForm.name" />
        </el-form-item>
        <el-form-item label="性别">
          <el-radio-group v-model="ruleForm.sex">
            <el-radio value="男">男</el-radio>
            <el-radio value="女">女</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="学校:">
          <el-input v-model="ruleForm.school" />
        </el-form-item>
        <el-form-item label="个人简介:">
          <el-input v-model="ruleForm.desc" type="textarea" size="large" :rows="8"/>
        </el-form-item>
        <el-form-item>
        </el-form-item>
      </el-form>
    </div>
    <!-- 主体内容 -->
    <div class="content">
      <el-form
          ref="ruleFormRef"
          style="max-width: 600px"
          :model="ruleForm"
          :rules="rules"
          label-width="auto"
          class="demo-ruleForm"
          :size="formSize"
          status-icon
      >
        <el-form-item label="姓名" prop="name">
          <el-input v-model="ruleForm.name" />
        </el-form-item>
        <el-form-item label="性别" prop="sex">
          <el-radio-group v-model="ruleForm.sex">
            <el-radio value="男">男</el-radio>
            <el-radio value="女">女</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="年龄" prop="age">
          <el-input v-model="ruleForm.age" />
        </el-form-item>
        <el-form-item label="学校" prop="school">
          <el-input v-model="ruleForm.school" />
        </el-form-item>
        <el-form-item label="专业" prop="profession">
          <el-input v-model="ruleForm.profession" />
        </el-form-item>
        <el-form-item label="手机" prop="phone">
          <el-input v-model="ruleForm.phone" />
        </el-form-item>
        <el-form-item label="邮件" prop="email">
          <el-input v-model="ruleForm.email" :disabled="true" />
        </el-form-item>
        <el-form-item label="地址" prop="address">
          <el-input v-model="ruleForm.address" />
        </el-form-item>
        <el-form-item label="个人简介:">
          <el-input v-model="ruleForm.desc" type="textarea" size="large" :rows="4"/>
        </el-form-item>
        <el-form-item class="bnt">
          <el-button type="primary" @click="submitForm(ruleFormRef)">
            提交更改
          </el-button>
          <el-button @click="resetForm(ruleFormRef)">取消</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<style scoped lang="scss">
.conatainer {
  display: flex;
  width: 100vw;
  height:100vh;
}
.userInfo {
  display: flex;
  flex-direction: column; /* 修改为垂直排列 */
  align-items: center; /* 居中对齐 */
  width: 20%;
  height: 75%;
  border-radius: 10px;
  margin-top:50px;
  margin-left: 250px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  background-color: #ffffff;
  .avatar {
    height: 100px;
    width: 100px;
    border-radius: 50%;
    margin-top: 50px;
  }
}

.content {
  margin-top:50px;
  margin-left: 50px;
  width: 50%;
  height: 75%;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  background-color: #ffffff;
}
.demo-ruleForm{
  margin-top: 50px;
  margin-left:50px;
}
.bnt{
    margin-top:20px;
    margin-left:20px;
}
</style>
