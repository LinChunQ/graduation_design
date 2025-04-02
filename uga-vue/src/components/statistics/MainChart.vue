<script setup>
import { ref, computed, watch, onMounted, onUnmounted } from 'vue';
import * as echarts from 'echarts';
import {getMainOption} from './echartsOption.vue'
 

// 是否为样本数据
const isSample = ref(true);

// 计算属性
const data = ref('')


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
    <div id="app">
        <div style="height: 90px; width: 36%; float: left;">
            正态分布曲线函数： `f(x) = (1 / (\sqrt {2\pi} \sigma)) e^(-(x-\mu)^2/(2\sigma^2))`
            <span style="color:blue">
                其中:
                `\mu` ：数学期望
                `\sigma` ：标准差
            </span>
        </div>
        <div style="height: 90px; float: left; padding-left: 450px;">
            <p>总长度：{{ data.length }}</p>
            <p>总 和： {{ sum }}</p>
            <p>平均值：{{ average }}</p>
            <p>最大值：{{ max }}</p>
            <p>最小值：{{ min }}</p>
            <p>{{ isSample ? '样本' : '总体' }}方差：{{ variance }}</p>
            <p>{{ isSample ? '样本' : '总体' }}标准差：{{ standardDeviation }}</p>
            <p>一倍标准差范围：{{ standarDevRangeOfOne.low + " ~ " + standarDevRangeOfOne.up }}</p>
            <p>二倍标准差范围：{{ standarDevRangeOfTwo.low + " ~ " + standarDevRangeOfTwo.up }}</p>
            <p>三倍标准差范围：{{ standarDevRangeOfThree.low + " ~ " + standarDevRangeOfThree.up }}</p>
        </div>
       
        <div ref="chart" id="chart" style="width: 866px; height: 762px;"></div>
    </div>
</template>

<style scoped>
/* 添加样式 */
</style>