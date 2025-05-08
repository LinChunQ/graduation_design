import { color } from "echarts";

//雷达图
const radarOption = {
    legend: {
      data: ['均分'],
      left:'right',
      textStyle: {
        fontSize: 16 ,
        color: '#fff'
      }
    },
    radar: {
      indicator: [
        { name: '题一', max: 20 },
        { name: '题二', max: 20 },
        { name: '题三', max: 20 },
        { name: '题四', max: 20 },
        { name: '题五', max: 20 },
        { name: '题六', max: 20 }
      ],
      name: {
        textStyle: {
          fontSize: 16 ,
          color: '#fff'
        }
      }
    },
    series: [
      {
        name: '等分率',
        type: 'radar',
        itemStyle: {
            color: 'green' // 改变线的颜色为绿色
          },
          label: {
            show: true,
            fontSize: 16,
            color: '#000'
          },
        data: [
          {
            value: [13, 15,16, 14, 17, 18],
            name: '均分'
          },
        ]
      }
    ]
  };


//饼图
const pieOption={
    legend: {
      top: '92%',
       textStyle: {
          fontSize: 14, // 调整字体大小
           color: '#fff' // 调整字体颜色
        }
    },
    series: [
      {
        name: 'Nightingale Chart',
        type: 'pie',
        radius: [20, 120],
        center: ['50%', '50%'],
        roseType: 'area',
        itemStyle: {
          borderRadius: 8
        },
        data: [
          { value: 40, name: '题6' },
          { value: 38, name: '题5' },
          { value: 32, name: '题3' },
          { value: 30, name: '题4' },
          { value: 28, name: '题2' },
          { value: 26, name: '题1' },
        ]
      }
    ]
  };


//主区的正态分布图
function getMainOption(data){
    // 是否为样本数据
    const isSample = ref(true);

    const dataOrderBy = computed(() => {
        const dataCopy = data.value.concat([]);
        return dataCopy.sort((a, b) => a - b);
    });
    
    const dataAfterClean = computed(() => {
        let res = {};
        for (let i = 0; i < data.value.length; i++) {
            let key = parseFloat(data.value[i]).toFixed(1);
            if (key !== "NaN" && parseFloat(key) === 0) key = "0.0";
            if (res[key]) res[key] += 1;
            else res[key] = 1;
        }
        return res;
    });
    
    const dataAfterCleanX = computed(() => {
        return Object.keys(dataAfterClean.value).sort((a, b) => a - b).map(t => parseFloat(t).toFixed(1));
    });
    
    const dataAfterCleanY = computed(() => {
        let r = [];
        for (let i = 0; i < dataAfterCleanX.value.length; i++) {
            r.push(dataAfterClean.value[dataAfterCleanX.value[i]]);
        }
        return r;
    });
    
    const dataAfterCleanXSub = computed(() => {
        let r = [];
        for (let i = parseFloat(min.value.toFixed(1)); i <= parseFloat(max.value.toFixed(1)); i += 0.01) {
            r.push(i.toFixed(2));
        }
        return r;
    });
    
    const sum = computed(() => {
        if (data.value.length === 0) return 0;
        return data.value.reduce((prev, curr) => prev + curr);
    });
    
    const average = computed(() => {
        return sum.value / data.value.length;
    });
    
    const median = computed(() => {
        const dataCopy = dataOrderBy.value;
        return (dataCopy[(dataCopy.length - 1) >> 1] + dataCopy[dataCopy.length >> 1]) / 2;
    });
    
    const deviation = computed(() => {
        const avg = average.value;
        return data.value.map(x => x - avg);
    });
    
    const variance = computed(() => {
        if (data.value.length === 0) return 0;
        const dev = deviation.value;
        const sumOfSquOfDev = dev.map(x => x * x).reduce((x, y) => x + y);
        return sumOfSquOfDev / (isSample.value ? (data.value.length - 1) : data.value.length);
    });
    
    const standardDeviation = computed(() => {
        return Math.sqrt(variance.value);
    });
    
    const standarDevRangeOfOne = computed(() => {
        return {
            low: average.value - 1 * standardDeviation.value,
            up: average.value + 1 * standardDeviation.value
        };
    });
    
    const standarDevRangeOfTwo = computed(() => {
        return {
            low: average.value - 2 * standardDeviation.value,
            up: average.value + 2 * standardDeviation.value
        };
    });
    
    const standarDevRangeOfThree = computed(() => {
        return {
            low: average.value - 3 * standardDeviation.value,
            up: average.value + 3 * standardDeviation.value
        };
    });
    
    const min = computed(() => {
        return Math.min.apply(null, data.value);
    });
    
    const max = computed(() => {
        return Math.max.apply(null, data.value);
    });
    
    const normalDistribution = computed(() => {
        let res = [];
        for (let i = 0; i < dataAfterCleanX.value.length; i++) {
            const x = dataAfterCleanX.value[i];
            const a = standardDeviation.value;
            const u = average.value;
            const y = (1 / (Math.sqrt(2 * Math.PI) * a)) * (Math.exp(-1 * ((x - u) * (x - u)) / (2 * a * a)));
            res.push(y);
        }
        return res;
    });
    
const mainOption = {
    legend: {
        data: ['f(x)'],
        top: '94%',
        textStyle: {
            fontSize: 14,
            color: '#fff'
        }
    },
    xAxis: [{
        data: dataAfterCleanX.value,
    }],
    yAxis: [{
        type: 'value',
        name: '频数',
        position: 'left',
        splitLine: {
            show: false
        },
        axisLine: {
            lineStyle: {
                color: 'orange'
            }
        },
        axisLabel: {
            formatter: '{value}'
        }
    }, {
        type: 'value',
        name: '概率',
        position: 'right',
        splitLine: {
            show: false
        },
        axisLine: {
            lineStyle: {
                color: '#fff'
            }
        },
        axisLabel: {
            formatter: '{value}'
        }
    }],
    series: [{
        name: '源数据',
        type: 'bar',
        yAxisIndex: 0,
        barGap: 0,
        barWidth: 27,
        itemStyle: {
            normal: {
                show: true,
                color: 'rgba(255, 204, 0,.3)',
                borderColor: '#FF7F50'
            }
        },
        data: dataAfterCleanY.value,
    }, {
        name: '正态分布',
        type: 'line',
        smooth: true,
        yAxisIndex: 1,
        data: normalDistribution.value,
        lineStyle:{
            color:"#91cc75"
        },
        markLine: {
            symbol: ['none'],
            lineStyle: {
                type: "silent",
                color: "green",
            },
            itemStyle: {
                normal: {
                    show: true,
                    color: 'black'
                }
            },
            label: {
                show: true,
                position: "middle"
            },
            data: [{
                name: '一倍标准差',
                xAxis: standarDevRangeOfOne.value.low.toFixed(1),
                lineStyle: {
                    opacity: (min.value > standarDevRangeOfOne.value.low) ? 0 : 1
                },
                label: {
                    show: !(min.value > standarDevRangeOfOne.value.low)
                }
            }, {
                name: '一倍标准差',
                xAxis: standarDevRangeOfOne.value.up.toFixed(1),
                lineStyle: {
                    opacity: (max.value < standarDevRangeOfOne.value.up) ? 0 : 1
                },
                label: {
                    show: !(max.value < standarDevRangeOfOne.value.up)
                }
            }, {
                name: '二倍标准差',
                xAxis: standarDevRangeOfTwo.value.low.toFixed(1),
                lineStyle: {
                    opacity: (min.value > standarDevRangeOfTwo.value.low) ? 0 : 1
                },
                label: {
                    show: !(min.value > standarDevRangeOfTwo.value.low)
                }
            }, {
                name: '二倍标准差',
                xAxis: standarDevRangeOfTwo.value.up.toFixed(1),
                lineStyle: {
                    opacity: (max.value < standarDevRangeOfTwo.value.up) ? 0 : 1
                },
                label: {
                    show: !(max.value < standarDevRangeOfTwo.value.up)
                }
            }, {
                name: '三倍标准差',
                xAxis: standarDevRangeOfThree.value.low.toFixed(1),
                lineStyle: {
                    opacity: (min.value > standarDevRangeOfThree.value.low) ? 0 : 1
                },
                label: {
                    show: !(min.value > standarDevRangeOfThree.value.low)
                }
            }, {
                name: '三倍标准差',
                xAxis: standarDevRangeOfThree.value.up.toFixed(1),
                lineStyle: {
                    opacity: (max.value < standarDevRangeOfThree.value.up) ? 0 : 1
                },
                label: {
                    show: !(max.value < standarDevRangeOfThree.value.up)
                }
            }, {
                name: '平均值',
                xAxis: average.value.toFixed(1),
                lineStyle: {
                    color: 'red'
                }
            }]
        }
    }]
};


return mainOption;
}


//柱状图
const barOption={
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'shadow'
      }
    },
    textStyle:{
        color:'#f1f1f1'
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '1%',
      containLabel: true
    },
    
    xAxis: [
      {
        type: 'category',
        
        data: ['0~59', '60~79', '80~100'],
        axisTick: {
          alignWithLabel: true
        }
      }
    ],
    yAxis: [
      {
        type: 'value',
        name: "人数",
        nameLocation: "end",
      },
      
    ],
    series: [
      {
        name: '人数',
        type: 'bar',
        barWidth: '40%',
        data: [16, 22, 10]
      },
      
    ],
  };
export{radarOption,pieOption,barOption,getMainOption}