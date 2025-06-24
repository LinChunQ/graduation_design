<script setup>
import useUserStore from '@/stores/useStoreUser'
const userStore=useUserStore()
const props=defineProps({course_id:''})
const course_id=ref(1);
const config = reactive({
  header: ['学号', '姓名', '题一',"题二","题三","题四","题五","题六","总分"],
  data: [],
  index: false,
  columnWidth: [120,80,60,60,60,60,60,60,60],
  headerBGC:"transparent",
  oddRowBGC:"transparent",
  evenRowBGC:"transparent",
  headerHeight:30,
  rowNum:10,
  align: ['left'],
})

onMounted(()=>{
  userStore.getTestPaper({'currentPage':0,'pageSize':0,'course_id':course_id.value});
})

watch(props.course_id,(newVal)=>{
    course_id.value=newVal.value;
    userStore.getTestPaper({'currentPage':0,'pageSize':0,'course_id':course_id.value});
})

watch(userStore.testPaperData, (newVal) => {
  if (newVal.data.length != 0) {
    // 对数据按 total 进行降序排序
    const sortedData = newVal.data.sort((a, b) => b.total - a.total);
    // 映射数据到所需的二维数组格式
    config.data = sortedData.map(item => [
      item.stu_no,
      item.stu_name,
      item.p1,
      item.p2,
      item.p3,
      item.p4,
      item.p5,
      item.p6,
      item.total
    ]);
  } else {
    config.data = [];
  }
})
</script>

<template>
<div class="table-container">
    <div class="table-header">
        <div class="dot"><div class="inner"></div></div>
        <div class="table-title">成绩排名</div>
    </div>
    <div class="table-content">
        <dv-scroll-board :config="config" style="width:100%;height:330px"/>
    </div>
</div>
</template>

<style scoped lang="scss">
.table-container{
    margin-top:3%;
    display:flex;
    flex-direction:column;
    height:100%;
    width:100%;
    overflow:hidden;
}

.table-header{
    display:flex;
    margin-left:2%;
    padding:10px;
    .table-title{
        margin-left:3px;
        color:#fff;
        font-size:18px;
        font-weight:600;
    }
}

.table-content{
    
}

.dot{
        display:flex;
        justify-content:center;
        height:10px;
        width:10px;
        padding:3px;
        border:2px solid #fff;
        border-radius:50%;
        .inner{
            height:10px;
            width:10px;
            border-radius:50%;
            background-color: #fff;
        }
}
::v-deep .header-item,
::v-deep .ceil{
  font-size: 13px;
}
</style>