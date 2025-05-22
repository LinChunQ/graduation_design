<script setup>
import { computed, reactive, ref } from 'vue'
import useUserStore from '@/stores/useStoreUser'
import {getTestByCourseId} from '@/apis/user'
const userStore=useUserStore()
const search = ref('')
const filterTableData = computed(() =>
  tableData.filter(
    (data) =>
      !search.value ||
      data.name.toLowerCase().includes(search.value.toLowerCase())
  )
)

const optionVal = ref('')
const options =reactive([])
const tableData = reactive([])
const allTableData =reactive([])
const currentPage = ref(1)
const pageSize = ref(12)
const total = ref(0) // 总记录数

const fields=ref({'学院':'college','班级':'stu_class','学号':'stu_no',
              '姓名':'stu_name','题目一':'p1','题目二':'p2',
              '题目三':'p3','题目四':'p4','题目五':'p5','题目六':'p6','总分':'total'})
const handleEdit = (index, row) => {
  console.log(index, row)
}
const handleDelete = (index, row) => {
  console.log(index, row)
}

const fetchTestPaper = async () => {
  const params = {
    pageSize: pageSize.value,
    currentPage: currentPage.value,
    course_id: optionVal.value || 0
  };
  userStore.getTestPaper(params);
}

const handleCurrentChange = (newPage) => {
  currentPage.value = newPage;
  fetchTestPaper();
}

const handlePrevClick = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
    fetchTestPaper();
  }
}

const handleNextClick = () => {
  if (currentPage.value < total.value) {
    currentPage.value++;
    fetchTestPaper();
  }
}

const handleExportData= async()=>{
  const params = {
    pageSize: 999,
    currentPage: currentPage.value,
    course_id: optionVal.value || 0
  };
  const res=await getTestByCourseId(params);
  allTableData.length=0;
  Object.assign(allTableData,res.data)
}

onMounted(()=>{
    if(!optionVal.value){
        fetchTestPaper();
    }
    userStore.getCourse()
    handleExportData();
})

watch(userStore.testPaperData,(newVal)=>{
    if(newVal.data.length!=0){
      Object.assign(tableData,newVal.data)
      total.value=newVal.total_items
    }else{
      tableData.length=0;
      total.value=0;
    }
})

watch(optionVal,(newVal)=>{
    userStore.getTestPaper({course_id:newVal});
    handleExportData();
})

watch(userStore.courseList,(newVal)=>{
    Object.assign(options,newVal)
    handleExportData();
})

</script>
<template>
<div class="his-container">
    <!-- 数据主页面 -->
        <div class="mainarea">
            <!-- 选择框 -->
        <div class="optionCourse">
            <el-select
              v-model="optionVal"
              placeholder="请选择课程"
              size="large"
              style="width: 25%"
              >
              <el-option
                  v-for="item in options"
                  :key="item.course_id"
                  :label="item.course_name"
                  :value="item.course_id"
              />
            </el-select>
            <vue3-json-excel
              :json-data="allTableData"
              :fields="fields"
              name="学生成绩表.xls"
            >
            <el-button type="success" plain size="large">
              导出数据<el-icon class="el-icon--right"><Upload /></el-icon>
            </el-button>
            </vue3-json-excel>
        </div>
        <!-- 数据表 -->
        <div class="data">
            <el-table 
                :data="filterTableData" 
                style="width: 100%"
                :cell-style="{ textAlign: 'center' }"
                :header-cell-style="{textAlign: 'center'}"
                >
                <el-table-column label="学院" prop="college" width="120%"/>
                <el-table-column label="班级" prop="stu_class" width="120%" />
                <el-table-column label="学号" prop="stu_no" width="120%" />
                <el-table-column label="姓名" prop="stu_name" width="120%"/>
                <el-table-column label="题目一" prop="p1" width="80%"/>
                <el-table-column label="题目二" prop="p2" width="80%"/>
                <el-table-column label="题目三" prop="p3" width="80%"/>
                <el-table-column label="题目四" prop="p4" width="80%"/>
                <el-table-column label="题目五" prop="p5" width="80%"/>
                <el-table-column label="题目六" prop="p6" width="80%"/>
                <el-table-column label="成绩" prop="total" width="80%"/>
                <el-table-column align="right" width="auto">
                <template #header>
                    <el-input v-model="search" size="small" placeholder="输入学号搜索试卷!" />
                </template>
                <template #default="scope">
                    <el-button size="small" @click="handleEdit(scope.$index, scope.row)">
                    修改
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
        </div>
        <el-pagination 
            background 
            layout="prev, pager, next" 
            :total="total"
            :current-page="currentPage" 
            :page-size="pageSize"
            @current-change="handleCurrentChange"
            @prev-click="handlePrevClick"
            @next-click="handleNextClick"/>
        </div>
    
</div>
</template>

<style scoped lang="scss">
.his-container{
    display:flex;
    justify-content:flex-start;
    height:100%;
    width: 100%;
    overflow: hidden;
}

.optionCourse{
  display: flex;
  margin-bottom:10px;
  justify-content: space-between;
}
.data{
    margin-bottom:20px;
}
.mainarea{
    margin-top:1%;
    width:80vw;
    height: 90%;
    margin-left:10%;
    padding:10px;
    border-radius:10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
    background-color:#fff;
    overflow: auto;
}

</style>