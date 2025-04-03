<script setup>
import useUserStore from '@/stores/useStoreUser'
import {pieOption} from './echartsOption.js'
import * as echarts from 'echarts'; // 引入 ECharts
const userStore=useUserStore()


function  initChart(){
    const chartDom = document.getElementById('pie');
    if(chartDom){
        const myChart = echarts.init(chartDom);
        let option=pieOption;
        myChart.setOption(option);
    }
}

onMounted(()=>{
    initChart();
})

</script>

<template>
    <div class="pie-container">
        <div class="pie-header">
            <div class="dot"><div class="inner"></div></div>
            <div class="pie-title">分数占比</div>
        </div>
        <div class="pie-content">
            <div id='pie'></div>
        </div>
    </div>
</template>
    
<style scoped lang="scss">
    .pie-container{
        margin-top:3%;
        display:flex;
        flex-direction:column;
        height:100%;
        width:100%;
        overflow:hidden;
    }
    
    .pie-header{
        display:flex;
        margin-left:2%;
        padding:10px;
        .pie-title{
            margin-left:3px;
            color:#fff;
            font-size:18px;
            font-weight:600;
        }
    }
    
    .pie-content{
        display:flex;
        justify-content:center;
        #pie{
            margin-top:-4%;
         width:25vw;
         height:35vh;
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