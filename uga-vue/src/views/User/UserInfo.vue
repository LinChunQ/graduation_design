<script setup>
import { ref, onMounted, reactive } from 'vue';
import {storeToRefs} from 'pinia'
import userAvatar from '@/assets/imgs/avatar.jpeg'
import  useUserStore  from '../../stores/useStoreUser'
import useAuthStore from '../../stores/useStoreAuth'
const userStore = useUserStore()
const authStore=useAuthStore()
const ruleFormRef = ref()
const ruleForm = reactive(userStore.userInfo)
const dialogFormVisible = ref(false)
const formLabelWidth = '140px'
const keyFlag=ref('add') //用于添加和编辑复用
const dialogTitle=ref('创建课程')

const form = reactive({
  course_name:'',
  stu_count:'',
  submit_count:''
})

const role=reactive({
  '0':'管理员',
  '1':'普通用户'
})

//个人信息表单规则
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
  email: [
    { required: true, message: '请输入邮箱!', trigger: 'blur' },
  ],
  desc: [
    { required: true, message: '请输入描述信息', trigger: 'blur' },
  ],
})

//课程信息
const tableData=reactive([{}])



//课程模块
const search = ref('')
const filterTableData = computed(() =>
  tableData.filter(
    (data) =>
      !search.value ||
      data.course_name.toLowerCase().includes(search.value.toLowerCase())
  )
)

const handleEdit = (index, row) => { //编辑课程
  keyFlag.value='edit';
  dialogTitle.value='编辑课程'
  dialogFormVisible.value =true;
  Object.assign(form,row);
 
}

async function changeCourse(){
      await userStore.editCourse(form)
      await userStore.getCourse()
      dialogFormVisible.value=false;
       //将资源还给创建
      keyFlag.value='add';
      dialogTitle.value="创建课程"
}
async function handleDelete (index, row){ //删除课程
  await userStore.deleteCourse(row)
  tableData.splice(index,1)
}

async function addCourse(){
  await userStore.addCourse(form)
  await userStore.getCourse()
  dialogFormVisible.value = false

}


const submitForm = async (formEl) => { //提交个人信息
  if (!formEl) return;
  await formEl.validate((valid, fields) => {
    if (valid) {
      userStore.updateUserInfo({"userInfo":ruleForm,"role":authStore.role});
    } else {
      console.log('error submit!', fields)
    }
  })
}

const resetForm = (formEl) => { //重置个人信息表单
  if (!formEl) return
  formEl.resetFields()
}

onMounted(()=>{
  userStore.getCourse();
})

watch(userStore.userInfo,(newVal)=>{
  Object.assign(ruleForm,newVal)
})

watch(userStore.courseList,(newVal)=>{
  Object.assign(tableData,newVal)
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
      <el-form-item label="用户类型" prop="name">
          <el-input v-model="role[authStore.role]"  disabled/>
        </el-form-item>
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
        <el-form-item label="专业" prop="profession" v-show="authStore.role==1">
          <el-input v-model="ruleForm.profession" />
        </el-form-item>
        <el-form-item label="手机" prop="phone">
          <el-input v-model="ruleForm.phone" disabled />
        </el-form-item>
        <el-form-item label="邮箱" prop="email">
          <el-input v-model="ruleForm.email" :disabled="true"/>
        </el-form-item>
        <el-form-item label="地址" prop="address">
          <el-input v-model="ruleForm.address" />
        </el-form-item>
        <el-form-item label="个人简介:" v-show="authStore.role==1">
          <el-input v-model="ruleForm.desc" type="textarea" size="large" :rows="4" />
        </el-form-item>
        <el-form-item class="bnt" >
          <el-button type="primary" @click="submitForm(ruleFormRef)">
            提交更改
          </el-button>
          <el-button @click="resetForm(ruleFormRef)">取消</el-button>
        </el-form-item>
      </el-form>
    </div>


     <!-- 侧边栏展示课程 -->
     <div class="user-course" v-show="authStore.role==1">
      <el-table 
        :data="filterTableData" 
        style="width: 100%"
        :cell-style="{ textAlign: 'center' }"
        :header-cell-style="{textAlign: 'center'}"
      >
        <el-table-column label="课程名称" prop="course_name" />
        <el-table-column label="学生人数" prop="stu_count" />
        <el-table-column label="批改人数" prop="submit_count" />
        <el-table-column align="right">
          <template #header>
            <el-input v-model="search" size="small" placeholder="搜索我的课程" />
          </template>
          <template #default="scope">
            <el-button size="small" @click="handleEdit(scope.$index, scope.row)">
              编辑
            </el-button>
            <el-button
              size="small"
              type="danger"
              @click="handleDelete(scope.$index, scope.row)"
            >
              删除
            </el-button>
          </template>
        </el-table-column>
      </el-table>

      <el-button plain @click="dialogFormVisible = true" style="margin-top:30px;">
        创建课程
      </el-button>
    </div>
  </div>

  <!-- 对话框 -->
  <el-dialog v-model="dialogFormVisible" :title="dialogTitle" width="500">
    <el-form :model="form">
      <el-form-item label="课程名称" :label-width="formLabelWidth">
        <el-input v-model="form.course_name" autocomplete="off" />
      </el-form-item>
      <el-form-item label="课程人数" :label-width="formLabelWidth">
        <el-input v-model="form.stu_count" autocomplete="off" />
      </el-form-item>
      <el-form-item label="批改人数" :label-width="formLabelWidth">
        <el-input v-model="form.submit_count" autocomplete="off" />
      </el-form-item>
    </el-form>
    <template #footer>
      <div class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取消</el-button>
        <el-button type="primary" @click="addCourse" v-show="keyFlag=='add'">
          确认创建
        </el-button>
        <el-button type="primary" @click="changeCourse" v-show="keyFlag=='edit'">
          确认修改
        </el-button>
      </div>
    </template>
  </el-dialog>
</template>

<style scoped lang="scss">
.conatainer {
  display: flex;
  width: 100%;
  height:100%;
}
.user-course {
  display: flex;
  flex-direction:column;
  width: 35%;
  height: 75%;
  border-radius: 10px;
  margin-top:50px;
  margin-left: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  background-color: #ffffff;
  padding:20px;
}

.content {
  display:flex;
  flex-direction:column;
  margin-top:50px;
  margin-left: 5%;
  width: 40%;
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


</style>
