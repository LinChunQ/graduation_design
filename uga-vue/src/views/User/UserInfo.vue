<script setup>
import { ref, onMounted, reactive } from 'vue';
import {storeToRefs} from 'pinia'
import userAvatar from '@/assets/imgs/avatar.jpeg'
import  useUserStore  from '../../stores/useStoreUser'
const userStore = useUserStore()
const ruleFormRef = ref()
const ruleForm = reactive(userStore.userInfo)

//个人信息表单
const rules = reactive({
  nickname: [
    { required: true, message: '请输入姓名!', trigger: 'blur' },
    { min: 1, max: 15, message: '姓名长度2~15个!', trigger: 'blur' },
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
    { required: true, message: '请输入描述信息', trigger: 'blur' },
  ],
})

//课程信息
const tableData= [
  {
    course_name: '计算机网络',
    stu_count: 41,
    submit_count:36
  },
  {
    course_name: '数据结构',
    stu_count: 41,
    submit_count:36
  },
  {
    course_name: '计算机组成原理',
    stu_count: 41,
    submit_count:36
  },
  {
    course_name: '计算机操作系统',
    stu_count: 41,
    submit_count:36
  },
]



//课程模块
const tableRowClassName = ({row,rowIndex,}) => {
  if (rowIndex === 1) {
    return 'warning-row'
  } else if (rowIndex === 3) {
    return 'success-row'
  }
  return ''
}


const submitForm = async (formEl) => { //提交个人信息
  if (!formEl) return;
  await formEl.validate((valid, fields) => {
    if (valid) {
      userStore.updateUserInfo(ruleForm);
    } else {
      console.log('error submit!', fields)
    }
  })
}

const resetForm = (formEl) => { //重置个人信息表单
  if (!formEl) return
  formEl.resetFields()
}

watch(userStore.userInfo,(newVal)=>{
  Object.assign(ruleForm,newVal)
})

</script>

<template>
  <div class="conatainer">
   
    <!-- 主体内容 -->
    <div class="content">
      <el-form
          ref="ruleFormRef"
          style="max-width: 600px"
          :model="ruleForm"
          :rules="rules"
          label-width="auto"
          class="demo-ruleForm"
          size="default"
          status-icon
      >
        <el-form-item label="姓名" prop="name">
          <el-input v-model="ruleForm.nickname" />
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


     <!-- 侧边栏展示课程 -->
     <div class="user-course">
      <el-table
        :data="tableData"
        style="width: 90%"
        :row-class-name="tableRowClassName"
      >
        <el-table-column prop="course_name" label="课程名称" width="150%" />
        <el-table-column prop="stu_count" label="学生人数" width="80%" />
        <el-table-column prop="submit_count" label="批改数量"  width="80%"/>
      </el-table>
    </div>
  </div>
</template>

<style scoped lang="scss">
.conatainer {
  display: flex;
  width: 100vw;
  height:100vh;
}
.user-course {
  display: flex;
  width: 25%;
  height: 75%;
  border-radius: 10px;
  margin-top:50px;
  margin-left: 5%;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  background-color: #ffffff;
  padding:20px;
}

.content {
  display:flex;
  flex-direction:column;
  margin-top:50px;
  margin-left: 5%;
  width: 50%;
  height: 75%;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  background-color: #ffffff;
  padding:20px;
}
.demo-ruleForm{
  margin-top: 50px;
  margin-left:50px;
}
.bnt{
    margin-top:20px;
    margin-left:20px;
}

.el-table .warning-row {
  --el-table-tr-bg-color: var(--el-color-warning-light-9);
}
.el-table .success-row {
  --el-table-tr-bg-color: var(--el-color-success-light-9);
}
</style>
