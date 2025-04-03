<script setup>
import useUserStore from '@/stores/useStoreUser'
import {radarOption} from './echartsOption.js'
import * as echarts from 'echarts'; // 引入 ECharts
const userStore=useUserStore()


function  initChart(){
    const chartDom = document.getElementById('main');
    if(chartDom){
        const myChart = echarts.init(chartDom);
        let option=radarOption;
        myChart.setOption(option);
    }
}

onMounted(()=>{
    initChart();
})

</script>

<template>
<div class="radar-container">
    <div class="radar-header">
        <div class="dot"><div class="inner"></div></div>
        <div class="radar-title">得分率</div>
    </div>
    <div class="radar-content">
        <div id='main'></div>
    </div>
</div>
</template>

<style scoped lang="scss">
.radar-container{
    margin-top:3%;
    display:flex;
    flex-direction:column;
    height:100%;
    width:100%;
    overflow:hidden;
}

.radar-header{
    display:flex;
    margin-left:2%;
    padding:10px;
    .radar-title{
        margin-left:3px;
        color:#fff;
        font-size:18px;
        font-weight:600;
    }
}

.radar-content{
    display:flex;
    justify-content:center;
    #main{
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