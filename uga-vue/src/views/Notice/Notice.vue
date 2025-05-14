<script setup>
import { computed, onMounted } from 'vue'
import { addNotice,addNoticeType,getNotice,getNoticeType ,deleteNotice,deleteNoticeType} from '../../apis/sys'
const optVal1 = ref('')
const optVal2 = ref('')
const dialogFormVisible = ref(false)
const typeFormVisible = ref(false)
const formLabelWidth = '140px'
const currentPage = ref(1)
const pageSize = ref(10)
const total = ref(0) // 总记录数

const form = reactive({
  title: '',
  type: '',
  content: '',
})

const classify=ref([]);

const options1 =computed(()=>{return classify.value}) 
const tableData=ref([])

const handlType= async ()=>{
    await addNoticeType(form)
    getNoticeTypeList()
    typeFormVisible.value=false;
}

async function onSubmit(){
    await addNotice(form)
    getNoticeList()
    dialogFormVisible.value=false;
}

async function getNoticeList(){
    const res=await getNotice({
        pageSize: pageSize.value,
        currentPage: currentPage.value,
    })
    tableData.value=res.data
    total.value=res.total
}

async function getNoticeTypeList(){
    const res=await getNoticeType()
    classify.value=res
}

const handleCurrentChange = (newPage) => {
  currentPage.value = newPage;
  getNoticeList()
}

const handlePrevClick = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
    getNoticeList()
  }
}

const handleNextClick = () => {
  if (currentPage.value < total.value) {
    currentPage.value++;
    getNoticeList()
  }
}

function  openAddNotice(){
    resetForm()
    dialogFormVisible.value = true
}
const resetForm=()=>{
   form.title=''
   form.content=''
   form.type=''
}

const delNotice= (data)=>{
    ElMessageBox.confirm(
    '是否要删除此条公告?',
    '提示',
    {
      confirmButtonText: '确认',
      cancelButtonText: '取消',
      type: 'warning',
    }
  ).then(async() => { //确认删除
        await deleteNotice(data)
        getNoticeList()
    })
    
}

const delNoticeType= (data)=>{
    ElMessageBox.confirm(
    '是否要删除此条公告类型?',
    '提示',
    {
      confirmButtonText: '确认',
      cancelButtonText: '取消',
      type: 'warning',
    }
  ).then(async() => { //确认删除
        await deleteNoticeType(data)
        getNoticeTypeList()
    })
    
}

onMounted(()=>{
    getNoticeList()
    getNoticeTypeList()
})
</script>
<template>
<div class="n-container">
    <!-- 左边框 -->
    <div class="n-left">
        <div class="left-header">
            <div class="n-title">
                <div class="n-label"></div>
                <div class="n-font"><strong>公告分类</strong></div>
            </div>
            <el-button type="primary" plain @click="typeFormVisible=true">增加分类</el-button>
        </div>
        <div class="left-content">
            <el-card 
                style="max-width: 480px;background-color:transparent"
                shadow="hover"
            >
                <template #header>
                <div class="card-header">
                    <span>全部</span>
                </div>
                </template>
                <p v-for="(item,index) in classify" :key="index" class="text-item" @click="delNoticeType(item)">{{ item.name}}
                    <el-divider />
                </p>
            </el-card>
        </div>
    </div>
    <!-- 右边框 -->
    <div class="n-right">
        <div class="right-header">
            <div class="n-title">
                <div class="n-label"></div>
                <div class="n-font"><strong>公告列表</strong></div>
            </div>
            <div class="opt-type">
                <el-select
                    v-model="optVal1"
                    placeholder="选择公告类型"
                    size="large"
                    style="width: 240px"
                    >
                    <el-option
                        v-for="item in options1"
                        :key="item.id"
                        :label="item.name"
                        :value="item.id"
                    />
                </el-select>
            </div>
            <el-button type="primary" plain @click="openAddNotice">发布公告</el-button>
        </div>
        <!-- 表格 -->
        <div class="data">
            <el-table 
                :data="tableData" 
                style="width: 100%"
                :cell-style="{ textAlign: 'center' }"
                :header-cell-style="{textAlign: 'center'}"
                >
                <el-table-column label="序号" type="index" width="100%" />
                <el-table-column label="公告标题" prop="title" width="280%"/>
                <el-table-column label="发布人" prop="username" width="100%" />
                <el-table-column label="发布类型" prop="type" width="100%">
                    <template #default="scope">
                        <span>{{ classify.find(
                                (i) => i.id == scope.row.type
                            )?.name }}
                        </span>
                    </template>
                </el-table-column>
                <el-table-column label="发布时间" prop="create_time" width="150%"/>
                <el-table-column label="发布内容" prop="content" width="auto"/>
                <el-table-column label="操作">
                    <template #default="scope">
                        <el-button type="danger" @click="delNotice(scope.row)">删除</el-button>
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
            @next-click="handleNextClick" />
    </div>
</div>


<!-- 添加公告弹框 -->
<el-dialog v-model="dialogFormVisible" title="发布公告" width="500">
    <el-form :model="form">
      <el-form-item label="公告标题" :label-width="formLabelWidth">
        <el-input v-model="form.title" autocomplete="off" />
      </el-form-item>
      <el-form-item label="发布类型" :label-width="formLabelWidth">
        <el-select v-model="form.type" placeholder="选择发布类型">
          <el-option
            v-for="item in options1"
            :key="item.id"
            :label="item.name"
            :value="item.id"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="详细内容">
            <el-input v-model="form.content" type="textarea" :rows="6" />
        </el-form-item>
    </el-form>
    <template #footer>
      <div class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取消</el-button>
        <el-button type="primary" @click="onSubmit">
          发布
        </el-button>
      </div>
    </template>
  </el-dialog>

  <!-- 添加分类弹框 -->
<el-dialog v-model="typeFormVisible" title="添加公告类型" width="500">
    <el-form :model="form">
      <el-form-item label="公告类型" :label-width="formLabelWidth">
        <el-input v-model="form.type" autocomplete="off" />
      </el-form-item>
    </el-form>
    <template #footer>
      <div class="dialog-footer">
        <el-button @click="typeFormVisible = false">取消</el-button>
        <el-button type="primary" @click="handlType">
          添加
        </el-button>
      </div>
    </template>
  </el-dialog>
</template>
<style lang="scss" scoped>
.n-container{
    display:flex;
    align-items:center;
    justify-content:center;
    width:100%;
    height:100%;
    gap:10px;
    overflow:hidden;
}
.n-left{
    display:flex;
    flex-direction:column;
    width:20%;
    height:85%;
    box-shadow:  -2px -2px 10px 2px rgb(187, 187, 187);
    padding:10px;
    .left-header{
        display:flex;
        justify-content:space-between;
        align-items:center;
        height:10%;
        width:100%;
    }

    .left-content{
        height:70%;
        width:100%;
        .text-item{
            font-size:16px;
            letter-spacing:1px;
            &:hover{
                color:#94cfcc;
            }
        }
    }
}
.n-right{
    display:flex;
    flex-direction:column;
    width:70%;
    height:85%;
    box-shadow: rgb(187, 187, 187) 2px 2px 10px 2px;
    padding:10px;
    .right-header{
        display:flex;
        justify-content:flex-start;
        gap:5%;
        margin-top:1%;
        margin-bottom:1%;
    }
}

.n-title{
    display:flex;
    align-items:center;
    .n-label{
        height:20px;
        width:10px;
        background-color:#7894d3;
        margin-right:5px;
    }
}

:deep(.el-divider--horizontal){
    margin:5px;
}
</style>