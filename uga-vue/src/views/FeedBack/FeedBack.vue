<script setup>
import TopCard from '@/components/feedback/topCard.vue';
import { getFeedBack } from '../../apis/sys';
import { onMounted } from 'vue';
import { ro } from 'element-plus/es/locale/index.mjs';

const currentPage = ref(1)
const pageSize = ref(10)
const total = ref(0) // 总记录数

const topList=reactive([{id:1,title:"好评",num:0},{id:2,title:"差评",num:0},
                {id:3,title:"建议",num:0},{id:4,title:"其他",num:0}])

const tableData =ref([])

const form = reactive({})

function handleSelect(row){
    Object.assign(form,row)
    form.process=row.process==0?'未回复':'已回复'
    form.type=row.type==1?'好评':form.type==2?'差评':form.type==3?'建议':'其他'
}

function onSubmit(){
    debugger
    form.process='已回复'
    ElMessage({
    message: '操作成功!',
    type: 'success'
  })
}

async function getFeedBackList(){
    const res=await getFeedBack({
        pageSize: pageSize.value,
        currentPage: currentPage.value,
    })
    tableData.value=res.data
    total.value=res.total
    topList.map(item=>{
        if(item.id==1) item.num=res.good;
        else if (item.id==2) item.num=res.bad;
        else if (item.id==3) item.num=res.suggest;
        else if (item.id==4) item.num=res.other;
    })
    if(res.data.length!=0)
        handleSelect(res.data[0])
}

const handleCurrentChange = (newPage) => {
  currentPage.value = newPage;
  getFeedBackList()
}

const handlePrevClick = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
    getFeedBackList()
  }
}

const handleNextClick = () => {
  if (currentPage.value < total.value) {
    currentPage.value++;
    getFeedBackList()
  }
}

onMounted(()=>{
    getFeedBackList()
})
</script>

<template>
<div class="fb-container">
<div class="fb-top">
    <TopCard v-for="(item,index) in topList"
    :key="index"
    :title="item.title"
    :num="item.num"
    :id="item.id"
    />
</div>
<!-- 底部 -->
<div class="fb-bottom">
    <!-- 列表部分 -->
    <div class="list">
        <div class="list-header">
            <div class="n-title">
                <div class="n-label"></div>
                <div class="n-font"><strong>反馈列表</strong></div>
            </div>
        </div>
        <div class="list-data">
            <el-table 
            :data="tableData" 
            stripe 
            style="width: 100%"
            :cell-style="{ textAlign: 'center' }"
            :header-cell-style="{textAlign: 'center'}"
            @row-click="handleSelect"
            >
                <el-table-column label="序号"  type="index" width="80%" />
                <el-table-column prop="type" label="反馈类型" width="100%">
                    <template #default="scope">
                        <span>{{topList.find((item)=>
                            item.id == scope.row.type
                        ).title}}</span>
                    </template>
                </el-table-column>
                <el-table-column prop="content" label="反馈内容" width="auto"/>
                <el-table-column prop="process" label="反馈进度" width="100%">
                    <template #default="scope">
                        <span>{{process==0?'未回复':'已回复'}}</span>
                    </template>
                </el-table-column>
                <el-table-column prop="username" label="用户昵称" width="100%" />
                <el-table-column prop="user_email" label="用户邮箱" width="100%" />
                <el-table-column prop="create_time" label="反馈时间" width="200%" />
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
    <el-divider direction="vertical" border-style="double" />
    <!-- 回复部分 -->
    <div class="reply">
        <div class="reply-header">
            <div class="n-title">
                <div class="n-label"></div>
                <div class="n-font"><strong>回复</strong></div>
            </div>
            <div class="reply-content">
                <el-form :model="form" label-width="auto" style="max-width: 600px">
                <el-form-item label="反馈人">
                <el-input v-model="form.username"  disabled/>
                </el-form-item>
                <el-form-item label="反馈人邮箱">
                <el-input v-model="form.user_email"  disabled/>
                </el-form-item>
                <el-form-item label="反馈类型">
                <el-input v-model="form.type" disabled />
                </el-form-item>
                <el-form-item label="反馈进度">
                    <el-input v-model="form.process" disabled />
                </el-form-item>
                <el-form-item label="反馈信息">
                <el-input disabled v-model="form.content" type="textarea" />
                </el-form-item>
                <el-form-item label="回复信息">
                <el-input v-model="form.reply_content" type="textarea" />
                </el-form-item>
                <el-form-item>
                <el-button type="primary" @click="onSubmit">回复</el-button>
                <el-button>取消</el-button>
                </el-form-item>
            </el-form>
            </div>
        </div>
    </div>
</div>
</div>
</template>
<style scoped lang="scss">
.fb-container{
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    height:100%;
    width:100%;
    gap:20px;
    overflow:hidden;
}
.fb-top{
    display:flex;
    align-items:center;
    justify-content:center;
    width:90%;
    height:25%;
    margin-top: 1%;
    box-shadow:0px 0px 4px 1px #d4d3d3;
    border-radius:10px;
}
.fb-bottom{
    display:flex;
    justify-content:center;
    align-items:center;
    width:90%;
    height:65%;
    box-shadow:0px 0px 4px 1px #d4d3d3;
    border-radius:10px;
    overflow-y: hidden;
    .list{
        height:90%;
        width:60%;
        .list-data{
            margin-top:2%;
        }
    }
    .reply{
        height:90%;
        width:30%;
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

:deep(.el-divider--vertical){
    border-left: 1px var(--el-border-color) var(--el-border-style);
    display: inline-block;
    height: 1em;
    margin: 0 15px;
    position: relative;
    vertical-align: middle;
    width: 1px;
    height:30em;
}
</style>