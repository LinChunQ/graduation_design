<script setup>
import { ref, computed, watch, onMounted, onUnmounted } from 'vue';
import * as echarts from 'echarts';
import {getMainOption} from './echartsOption.js'
import {mockData} from './data.js'


// 计算属性
const data = ref(mockData)


// 生成 Echarts 图
const initChartsData = (ref) => {
    const chartDom = document.getElementById(ref);
    if (!chartDom) return;
    const chart = echarts.init(chartDom);
    const options=getMainOption(data)
    chart.setOption(options);
    window.addEventListener("resize", () => {
        chart.resize();
    });



// 清理事件监听器
onUnmounted(() => {
        window.removeEventListener("resize", () => {
            chart.resize();
        });
        chart.dispose();
    });
};

// 初始化数据
onMounted(() => {
    initChartsData('chart');
});
</script>

<template>
<div class="main-container">
    <div class="main-header">
        <div class="dot"><div class="inner"></div></div>
        <div class="main-title">高斯分布</div>
    </div>
    <div class="main-content">
        <div ref="chart" id="chart"></div>
    </div>
</div>
</template>

<style scoped>
.main-container{
    display:flex;
    flex-direction:column;
    height:100%;
    width:100%;
    overflow:hidden;
}
.main-header{
        display:flex;
        margin-left:2%;
        padding:10px;
        .main-title{
            margin-left:3px;
            color:#fff;
            font-size:18px;
            font-weight:600;
        }
}

.main-content{
    height:100%;
    width:98%;
    margin-left:1%;
    margin-top:5%;
    #chart{
       width:35vw;
       height: 50vh;
    }
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

</style>