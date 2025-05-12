<script setup>
import { computed, ref } from 'vue'
import useUserStore from '@/stores/useStoreUser'
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
const currentPage = ref(1)
const pageSize = ref(12)
const total = ref(0) // 总记录数
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


onMounted(()=>{
    if(!optionVal.value){
        fetchTestPaper();
    }
    userStore.getCourse()
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
})

watch(userStore.courseList,(newVal)=>{
    Object.assign(options,newVal)
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
    margin-bottom:10px;;
}
.data{
    margin-bottom:20px;
}
.mainarea{
    margin-top:1%;
    width:80vw;
    margin-left:10%;
    padding:10px;
    border-radius:10px;
    background-color:#fff;
    overflow: auto;
}

</style>