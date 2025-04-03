<script setup>
import useUserStore from '@/stores/useStoreUser'
import {barOption} from './echartsOption.js'
import * as echarts from 'echarts'; // 引入 ECharts
const userStore=useUserStore()


function  initChart(){
    const chartDom = document.getElementById('bar');
    const myChart = echarts.init(chartDom);
    myChart.setOption(barOption);
}

onMounted(()=>{
    initChart();
})

</script>

<template>
<div class="bar-container">
    <div class="bar-header">
        <div class="dot"><div class="inner"></div></div>
        <div class="bar-title">分数分析</div>
    </div>
    <div class="bar-content">
        <div id='bar'></div>
    </div>
</div>
</template>

<style scoped lang="scss">
.bar-container{
    margin-top:3%;
    display:flex;
    flex-direction:column;
    height:100%;
    width:100%;
    overflow:hidden;
}

.bar-header{
    display:flex;
    margin-left:2%;
    padding:10px;
    .bar-title{
        margin-left:3px;
        color:#fff;
        font-size:18px;
        font-weight:600;
    }
}

.bar-content{
    display:flex;
    justify-content:center;
    #bar{
     width:25vw;
     height:30vh;
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