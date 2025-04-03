<script setup>
import useUserStore from '@/stores/useStoreUser'
import RankTable from "@/components/statistics/RankTable.vue"
import RadarChart from "@/components/statistics/RadarChart.vue"
import RateChart from "@/components/statistics/RateChart.vue"
import BarChart from "@/components/statistics/BarChart.vue"
import MainChart from "@/components/statistics/MainChart.vue"
const userStore=useUserStore()
const optionVal = ref('')
const options =reactive([])

onMounted(()=>{
    userStore.getCourse()
})
watch(optionVal,(newVal)=>{
    userStore.getTestPaper({course_id:newVal});
})

watch(userStore.courseList,(newVal)=>{
    Object.assign(options,newVal)
})

</script>

<template>
<div class="sta-container">
<dv-border-box2>
    <div class="left">
        <dv-border-box12> 
            <RadarChart/>
        </dv-border-box12>
        <dv-border-box12>
            <RateChart/>
        </dv-border-box12>
    </div>
    <div class="middle">
        <dv-border-box12>
             <!-- 选择框 -->
            <div class="optionCourse">
                    <el-select
                        v-model="optionVal"
                        placeholder="请选择课程"
                        size="large"
                        style="width: 25%"
                        >
                        <el-option
                            v-for="item in options"
                            :key="item.course_id"
                            :label="item.course_name"
                            :value="item.course_id"
                        />
                    </el-select>
            </div>
            <!-- 图形 -->
             <MainChart/>
        </dv-border-box12>
    </div>
    <div class="right">
        <dv-border-box12>
            <div class="table">
                <RankTable
                :course_id="optionVal.value"/>
            </div>
        </dv-border-box12>
        <dv-border-box12>
            <BarChart/>
        </dv-border-box12>
    </div>
</dv-border-box2>
</div>
</template>
<style scoped lang="scss">
.sta-container{
  display: flex;
  justify-content:center;
  width: 100%;
  height: 100vh;  /* 使其填满整个屏幕 */
  background-image: url('@/assets/imgs/Home-background1.png'); /* 这里使用你的背景图路径 */
  background-size: cover;  /* 背景图覆盖整个区域 */
  background-position: center;  /* 背景居中 */
  background-repeat: no-repeat;  /* 防止背景重复 */
  overflow:hidden;
}

::v-deep .dv-border-box-2 .border-box-content {
    display:flex;
    justify-content:center;
}

.left{
    display:flex;
    flex-direction:column;
    height:80%;
    width:25%;
    margin-top:50px;
}
.middle{
    display:flex;
    flex-direction:column;
    height:80%;
    width:35%;
    margin-top:50px;
    .optionCourse{
        width:100%;
        margin-left:4%;
        margin-top:2%;
        background-color:transparent;
       :deep(.el-select--large .el-select__wrapper) {
            font-size: 14px;
            gap: 6px;
            line-height: 24px;
            min-height: 40px;
            padding: 8px 16px;
            background-color: transparent;
        }
    }

 :deep(.border-box-content){
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
}

}

.right{
    display:flex;
    flex-direction:column;
    height:80%;
    width:25%;
    margin-top:50px;
    .table{
    height:80%;
    width:100%;
 }
}



</style>