<script setup>
import {ref,watch} from 'vue'
import useUserStore from '@/stores/useStoreUser'
const userStore=useUserStore()
const tableData =ref([]);

const imageData = ref([]);

function uploadFile(item) {
    const formData = new FormData();
    formData.append('image', item.raw);
    userStore.smartGrading(formData)
    const imageUrl = URL.createObjectURL(item.raw); // 图片上传浏览器回显地址
    imageData.value.push({ url: imageUrl, name: item.name });
}

function handleCancel() {
    imageData.value=[];
}

function handleSubmit(){

}

watch(()=>userStore.singleGrade,(newVal)=>{
    tableData.value.push(newVal)
})

</script>

<template>
    <div class="container">
        <!-- 上传图片区域 -->
       <div class="uploadfile">
            <!-- 上传文件 -->
            <el-upload
                class="upload_img"
                accept="image/jpg,image/jpeg,image/png"
                drag
                action="#"
                :multiple="false"
                :show-file-list="false"
                :auto-upload="false"
                :on-change="uploadFile"
            >
                <el-icon class="el-icon--upload"><upload-filled /></el-icon>
                <div class="el-upload__text"> 拖动文件或 <em>点击上传</em></div>
                <template #tip>
                <div class="el-upload__tip" style="color: red">
                    jpg/png图像文件小于2mb
                </div>
                </template>
            </el-upload>
            <!-- 图片回显组 -->
            <div class="img-group">
                <div v-for="(image, index) in imageData" :key="index" class="image-item">
                    <el-image 
                        :src="image.url" 
                        style="width: 100px; height: 100px" 
                        :preview-src-list="[image.url]"
                        :fit="fit" />
                </div>
            </div>
            <!-- 按钮组 -->
            <div class="btn-group">
                <el-button type="primary" @click="handleSubmit">提交</el-button>
                <el-button type="danger" plain style="margin-left: 50px" @click="handleCancel">清理图片区域</el-button>
            </div>
            
       </div>
       <!-- 计算结果区域 -->
       <div class="result">
        <el-table class="res_table" :data="tableData" border>
            <el-table-column prop="stu_no" label="学号" width="95%" />
            <el-table-column prop="stu_name" label="姓名" width="80%" />
            <el-table-column prop="p1" label="题目一" width="70%"/>
            <el-table-column prop="p2" label="题目二" width="70%"/>
            <el-table-column prop="p3" label="题目三" width="70%"/>
            <el-table-column prop="p4" label="题目四" width="70%"/>
            <el-table-column prop="p5" label="题目五" width="70%"/>
            <el-table-column prop="p6" label="题目六" width="70%"/>
            <el-table-column prop="total" label="总分" />
        </el-table>
       </div>
    </div>
</template>

<style scoped lang="scss">
.container{
  display: flex;
  width: 100%;
  height:100%;
  margin-top:50px;
}

.uploadfile{
  width: 35%;
  height: 100%;
  min-height:600px;
  margin-left:100px;
  background-color: #ffffff;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  margin-top: 10px;
  border-radius: 4px;
}

.upload_img{
    width: 90%;
    margin-left: 25px;
    margin-top: 30px;
   // border: 1px solid #6b2a2a;
}
.result{
    width: 50%;
    height:100%;
    min-height:600px;
    margin-left:30px;
    background-color: #ffffff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    margin-top: 10px;
    border-radius: 4px;
}

.res_table{
    width: 95%;
    height:100%;
    margin-left: 12px;
    margin-top: 30px;
    color: #000000;
}
.img-group {
    width: 87%;
    min-height:200px;
    height: auto;
    padding: 10px;
    margin-left: 25px;
    margin-top: 20px;
    border: 0.3px solid #bebcbc;
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    grid-gap: 10px;
    justify-content: center;
}
.btn-group{
    margin-left: 25px;
    margin-top: 20px;
}
.image-item {
    width: 100px;
    height: 100px;
}
</style>