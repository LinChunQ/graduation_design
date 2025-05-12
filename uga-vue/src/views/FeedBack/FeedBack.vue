<script setup>
import TopCard from '@/components/feedback/topCard.vue';
const topList=[{id:0,title:"好评",num:22},{id:1,title:"差评",num:35},
                {id:2,title:"建议",num:46},{id:3,title:"其他",num:59}]

const tableData = [
  {
    id:"000000001",
    type:'好评',
    nickname:"李华",
    date: '2016-05-03',
    process:"未查看",
    content:'产品好用.............'
  },
  { id:"000000002",
    type:'建议',
    nickname:"李华",
    date: '2016-05-03',
    process:"未查看",
    content:'建议增加更多功能.............'
  },
  { id:"000000003",
    type:'差评',
    nickname:"李华",
    date: '2016-05-03',
    process:"未查看",
    content:'有bug.............'
  },
  { id:"000000004",
    type:'好评',
    nickname:"李华",
    date: '2016-05-03',
    process:"未查看",
    content:'产品好用.............'
  },
  { id:"000000005",
    type:'建议',
    nickname:"李华",
    date: '2016-05-03',
    process:"未查看",
    content:'建议增加更多功能.............'
  },
  { id:"000000006",
    type:'差评',
    nickname:"李华",
    date: '2016-05-03',
    process:"未查看",
    content:'有bug.............'
  },
//   { id:"000000007",
//     type:'好评',
//     nickname:"李华",
//     date: '2016-05-03',
//     process:"未查看",
//     content:'产品好用.............'
//   },
//   { id:"000000008",
//     type:'好评',
//     nickname:"李华",
//     date: '2016-05-03',
//     process:"未查看",
//     content:'产品好用.............'
//   },
]

const form = reactive({
    id:"000000008",
    type:'好评',
    nickname:"李华",
    date: '2016-05-03',
    process:"未查看",
    content:'产品好用.............'
})

function handleSelect(row){
    Object.assign(form,row)
}

function onSubmit(){
    debugger
    form.process='已回复'
    ElMessage({
    message: '操作成功!',
    type: 'success'
  })
}

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
                <el-table-column prop="type" label="反馈类型" width="100%" />
                <el-table-column prop="id" label="反馈id" width="100%" />
                <el-table-column prop="process" label="反馈进度" width="100%" />
                <el-table-column prop="nickname" label="用户昵称" width="100%" />
                <el-table-column prop="date" label="反馈时间" width="200%" />
                <el-table-column prop="content" label="反馈内容" width="auto" />
            </el-table>
        </div>
        <el-pagination background layout="prev, pager, next" :total="100" />
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
                <el-input v-model="form.nickname"  disabled/>
                </el-form-item>
                <el-form-item label="反馈id">
                <el-input v-model="form.id"  disabled/>
                </el-form-item>
                <el-form-item label="反馈类型">
                <el-input v-model="form.type" disabled />
                </el-form-item>
                <el-form-item label="反馈进度">
                <el-select disabled v-model="form.region" placeholder="未查看">
                    <el-option label="已查看" value="已查看" />
                    <el-option label="已处理" value="已处理" />
                </el-select>
                </el-form-item>
                <el-form-item label="反馈信息">
                <el-input disabled v-model="form.content" type="textarea" />
                </el-form-item>
                <el-form-item label="回复信息">
                <el-input v-model="form.desc" type="textarea" />
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