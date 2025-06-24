<template>
<div class="notic-bar">
      <img :src="notic" class="notice-img" />
      <div class="notice-bar-container">
        <div class="notice-bar__wrap">
          <div
            v-for="(item, index) in list"
            :key="index"
            class="notice-bar__wrap_text"
            @click="noticeClick(item)"
          >
            {{item.title}}
          </div>
        </div>
      </div>
</div>

<!-- 添加公告详情弹框 -->
<el-dialog v-model="dialogFormVisible" title="公告详情" width="500">
    <el-form :model="form" disabled>
      <el-form-item label="公告标题" :label-width="formLabelWidth">
        <el-input v-model="form.title" autocomplete="off" />
      </el-form-item>
      <el-form-item label="详细内容">
            <el-input v-model="form.content" type="textarea" :rows="6" />
        </el-form-item>
    </el-form>
    <template #footer>
      <div class="dialog-footer">
        <el-button @click="dialogFormVisible = false">关闭</el-button>
      </div>
    </template>
  </el-dialog>
</template>
   
<script setup>
import notic from "../../assets/icons/notice.png";
import {getNotice} from "../../apis/sys";
import { onMounted, onUnmounted } from "vue";

const list =ref([])
const dialogFormVisible = ref(false);
const form = reactive({
  title: '',
  content: '',
})

async function getNoticeList(){
    const res=await getNotice({
        pageSize: 0,
        currentPage: 0,
    })
    list.value=res
}

const noticeClick = (item) => {
  form.content = item.content;
  form.title = item.title;
  dialogFormVisible.value = true;
}

onMounted(()=>{
  getNoticeList()
})

</script>
   
<style lang="scss" scoped>
  .notic-bar {
    display: flex;
    justify-content:center;
    align-items:center;
    height:100%;
    width:80%;
    //background: #e7ebe5;
    background: transparent;
    border-radius: 20px;
    z-index: 10;
  }
  .notice-bar-container {
    display: flex;
    width: calc(100% - 30px);
    height: 20px;
    overflow: hidden;
    margin-left: 5px;
  }
  .notice-img {
    margin-left:10px;
    width: 20px;
    height: 20px;
  }
  .notice-bar__wrap {
    margin-left: 10px;
    display: flex;
    animation: move 30s linear infinite;
    white-space: nowrap; /* 防止换行 */
    line-height: 20px;
    // color: #000;
    color: #fff;
    .notice-bar__wrap_text {
      width: max-content;
      min-width: 100px;
      padding-right: 50px;
    }
  }
  .notice-bar__wrap:hover {
    animation-play-state: paused;
  }
  @keyframes move {
    0% {
    transform: translateX(100%);
  }
  100% {
    transform: translateX(-100%);
  }
  }
  </style>