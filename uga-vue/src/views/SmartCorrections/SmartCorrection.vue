<script setup>
const tableData = [
  {sno: '2021283101',name: 'Tom1',p1:8,p2:10,p3:10,p4:20,p5:20,p6:20,grade: 88,},
  {sno: '2021283102',name: 'Tom2',p1:9,p2:10,p3:10,p4:20,p5:20,p6:20,grade: 89,},
  {sno: '2021283103',name: 'Tom3',p1:12,p2:10,p3:10,p4:20,p5:20,p6:20,grade: 92,},
  {sno: '2021283104',name: 'Tom4',p1:11,p2:10,p3:10,p4:20,p5:20,p6:20,grade:91,},
]

let imageData = [
    {url:'https://cn.bing.com/images/search?q=%E5%9B%BE%E7%89%87&FORM=IQFRBA&id=42BE9CBF4E57BF77C86A597C9043710BF0AAC2F9',name:'1'},
    {url:'https://cn.bing.com/images/search?q=%E5%9B%BE%E7%89%87&FORM=IQFRBA&id=42BE9CBF4E57BF77C86A597C9043710BF0AAC2F9',name:'2'},
    {url:'https://cn.bing.com/images/search?q=%E5%9B%BE%E7%89%87&FORM=IQFRBA&id=42BE9CBF4E57BF77C86A597C9043710BF0AAC2F9',name:'3'},
    {url:'https://cn.bing.com/images/search?q=%E5%9B%BE%E7%89%87&FORM=IQFRBA&id=42BE9CBF4E57BF77C86A597C9043710BF0AAC2F9',name:'4'},
    {url:'https://cn.bing.com/images/search?q=%E5%9B%BE%E7%89%87&FORM=IQFRBA&id=42BE9CBF4E57BF77C86A597C9043710BF0AAC2F9',name:'5'},
    {url:'https://cn.bing.com/images/search?q=%E5%9B%BE%E7%89%87&FORM=IQFRBA&id=42BE9CBF4E57BF77C86A597C9043710BF0AAC2F9',name:'6'},
]
</script>

<template>
    <div class="container">
        <!-- 上传图片区域 -->
       <div class="uploadfile">
            <!-- 上传文件 -->
            <el-upload
                class="upload_img"
                drag
                action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
                multiple
            >
                <el-icon class="el-icon--upload"><upload-filled /></el-icon>
                <div class="el-upload__text">
                拖动文件或 <em>点击上传</em>
                </div>
                <template #tip>
                <div class="el-upload__tip" style="color: red">
                    jpg/png图像文件小于2mb
                </div>
                </template>
            </el-upload>
            <!-- 图片回显组 -->
            <div class="img-group">
                <div v-for="(image, index) in imageData" :key="index" class="image-item">
                    <el-image :src="image.url" style="width: 80px; height: 80px" />
                </div>
            </div>
            <!-- 按钮组 -->
            <div class="btn-group">
                <el-button type="primary" @click="handleSubmit">提交</el-button>
                <el-button type="danger" plain style="margin-left: 50px">取消</el-button>
            </div>
            
       </div>
       <!-- 计算结果区域 -->
       <div class="result">
        <el-table class="res_table" :data="tableData" border>
            <el-table-column prop="sno" label="学号" width="110" />
            <el-table-column prop="name" label="姓名" width="80" />
            <el-table-column prop="p1" label="题目一" width="70"/>
            <el-table-column prop="p2" label="题目二" width="70"/>
            <el-table-column prop="p3" label="题目三" width="70"/>
            <el-table-column prop="p4" label="题目四" width="70"/>
            <el-table-column prop="p5" label="题目五" width="70"/>
            <el-table-column prop="p6" label="题目六" width="70"/>
            <el-table-column prop="grade" label="总分" />
        </el-table>
       </div>
    </div>
</template>

<style scoped lang="scss">
.container{
  display: flex;
  width: 100vw;
  height:100vh;
}

.uploadfile{
  width: 35%;
  height: 90%;
  margin-left:85px;
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
    height:90%;
    margin-left:50px;
    background-color: #ffffff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    margin-top: 10px;
    border-radius: 4px;
}

.res_table{
    width: 95%;
    margin-left: 12px;
    margin-top: 10px;
    color: #000000;
}
.img-group{
    width: 90%;
    height:40%;
    margin-left: 25px;
    margin-top: 20px;
    border: 0.3px solid #bebcbc;
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 10px;
}
.btn-group{
    margin-left: 25px;
    margin-top: 20px;
}
.image-item {
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>