<script setup>

</script>

<template>
<div class="sta-container">
<dv-border-box2>
    <div class="left">
        <dv-border-box12>
        </dv-border-box12>
        <dv-border-box12>
        </dv-border-box12>
    </div>
    <div class="middle">
        <dv-border-box12>
        </dv-border-box12>
    </div>
    <div class="right">
        <dv-border-box12>
        </dv-border-box12>
        <dv-border-box12>
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
}
.right{
    display:flex;
    flex-direction:column;
    height:80%;
    width:25%;
    margin-top:50px;
}

</style>