<script setup>
import Good from '@/assets/imgs/feedback/good.png'
import Bad from '@/assets/imgs/feedback/bad.png'
import Suggestion from '@/assets/imgs/feedback/suggestion.png'
import Other from '@/assets/imgs/feedback/other.png'

const imgList={
    0:Good,
    1:Bad,
    2:Suggestion,
    3:Other
}
const props=defineProps({
    title:'',
    num:0,
    id:0
})
</script>

<template>
<div class="card-container">
    <div class="card-content">
        <div class="img-box">
            <img class="card-img" :src="imgList[props.id]"/>
        </div>
        <div class="card-title">{{ props.title }}</div>
        <div class="card-num">{{ props.num }}</div>
    </div>
</div>
</template>

<style lang="scss" scoped>
.card-container{
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    height:100%;
    width:25%;
    text-align:center;
    font-size:18px;
}
.card-img{
    height:50%;
    width:50%;
}
.card-num{
    margin-top:10px;
    font-size:20px;
    font-weight:600;
}

</style>