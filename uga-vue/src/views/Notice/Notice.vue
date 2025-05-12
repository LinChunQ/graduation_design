<script setup>

const optVal1 = ref('')
const optVal2 = ref('')
const dialogFormVisible = ref(false)
const typeFormVisible = ref(false)
const formLabelWidth = '140px'
const classfiy_type=ref("");
const form = reactive({
  name: '',
  region: '',
  date1: '',
  date2: '',
  delivery: false,
  type: [],
  resource: '',
  desc: '',
})

const classify=ref([{id:1,name:"活动通知"},{id:2,name:"功能通知"},
                {id:3,name:"版本更新"},{id:4,name:"紧急通知"}]);

const options1 =classify.value
const options2 =[{id:1,name:'全部用户'},{id:2,name:'测试用户'},{id:3,name:"内部用户"}]
const tableData=[{title:"版本已更新,赶快体验新功能!",name:"李华",scale:'全部用户',type:'定时发布',stat:"已发布",time:'2025-3-31 12:11:33'},
{title:"历史使用出现bug,暂停服务!",name:"管理员",scale:'内部用户',type:'定时发布',stat:"已发布",time:'2025-3-31 12:11:33'},
{title:"智能审批功能已上线,赶快体验新功能!",name:"李华",scale:'全部用户',type:'定时发布',stat:"未发布",time:'2025-3-31 12:11:33'},
{title:"历史使用功能已上线,赶快体验新功能!",name:"李华",scale:'测试用户',type:'定时发布',stat:"已发布",time:'2025-3-31 12:11:33'},
{title:"大促销活动,点击链接查看详情!",name:"李华",scale:'全部用户',type:'定时发布',stat:"已发布",time:'2025-3-31 12:11:33'},
{title:"大促销活动,点击链接查看详情!",name:"李华",scale:'全部用户',type:'定时发布',stat:"未发布",time:'2025-3-31 12:11:33'},
{title:"大促销活动,点击链接查看详情!",name:"李华",scale:'全部用户',type:'定时发布',stat:"已发布",time:'2025-3-31 12:11:33'},
{title:"版本已更新,赶快体验新功能!",name:"李华",scale:'全部用户',type:'定时发布',stat:"已发布",time:'2025-3-31 12:11:33'},
{title:"统计分析出现bug,暂停服务!",name:"管理员",scale:'全部用户',type:'定时发布',stat:"未发布",time:'2025-3-31 12:11:33'},
{title:"版本已更新,赶快体验新功能!",name:"李华",scale:'全部用户',type:'定时发布',stat:"已发布",time:'2025-3-31 12:11:33'}
]

const handlType=()=>{
    let len=classify.value.length;
    classify.value.push({id:len+1,name:classfiy_type.value})
    ElMessage({
    message: '操作成功!',
    type: 'success',
  })
    typeFormVisible.value=false;
}
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
                <p v-for="(item,index) in classify" :key="index" class="text-item">{{ item.name}}
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
            <div class="opt-type">
                <el-select
                    v-model="optVal2"
                    placeholder="选择公告范围"
                    size="large"
                    style="width: 240px"
                    >
                    <el-option
                        v-for="item in options2"
                        :key="item.id"
                        :label="item.name"
                        :value="item.id"
                    />
                </el-select>
            </div>
            <el-button type="primary" plain @click="dialogFormVisible = true">发布公告</el-button>
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
                <el-table-column label="发布人" prop="name" width="100%" />
                <el-table-column label="发布范围" prop="scale" width="100%" />
                <el-table-column label="发布类型" prop="type" width="100%"/>
                <el-table-column label="发布状态" prop="stat" width="100%"/>
                <el-table-column label="发布时间" prop="time" width="150%"/>
            </el-table>
        </div>
        <el-pagination background layout="prev, pager, next" :total="100" />
    </div>
</div>


<!-- 添加公告弹框 -->
<el-dialog v-model="dialogFormVisible" title="发布公告" width="500">
    <el-form :model="form">
      <el-form-item label="公告标题" :label-width="formLabelWidth">
        <el-input v-model="form.name" autocomplete="off" />
      </el-form-item>
      <el-form-item label="公告类型" :label-width="formLabelWidth">
        <el-select v-model="form.region" placeholder="选择公告类型">
          <el-option label="活动通知" value="1" />
          <el-option label="功能通知" value="2" />
        </el-select>
      </el-form-item>
      <el-form-item label="发布范围" :label-width="formLabelWidth">
        <el-select v-model="form.region" placeholder="选择发布范围">
          <el-option label="全部用户" value="1" />
          <el-option label="测试用户" value="2" />
        </el-select>
      </el-form-item>
      <el-form-item label="详细内容">
            <el-input v-model="form.desc" type="textarea" :rows="6" />
        </el-form-item>
    </el-form>
    <template #footer>
      <div class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取消</el-button>
        <el-button type="primary" @click="dialogFormVisible = false">
          发布
        </el-button>
      </div>
    </template>
  </el-dialog>

  <!-- 添加分类弹框 -->
<el-dialog v-model="typeFormVisible" title="添加公告类型" width="500">
    <el-form :model="form">
      <el-form-item label="公告类型" :label-width="formLabelWidth">
        <el-input v-model="classfiy_type" autocomplete="off" />
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