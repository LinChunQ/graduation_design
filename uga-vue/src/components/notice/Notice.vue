<template>
    <div class="notic-bar">
      <img :src="notic" class="notice-img" />
      <div class="notice-bar-container">
        <div class="notice-bar__wrap">
          <div
            v-for="(item, index) in list"
            :key="index"
            class="notice-bar__wrap_text"
          >
            {{ item }}
          </div>
        </div>
      </div>
    </div>
  </template>
   
  <script setup lang="ts">
  import notic from "../../assets/icons/notice.png";
  const list = [
    "版本已更新,赶快体验新功能!",
    "",
    "智能审批功能已上线,赶快体验新功能!",
    "",
    "历史使用功能已上线,赶快体验新功能!",
    "",
    "大促销活动,点击链接查看详情!",
  ];
  </script>
   
  <style lang="scss" scoped>
  .notic-bar {
    display: flex;
    justify-content:center;
    align-items:center;
    height:100%;
    width:80%;
    background: #e7ebe5;
    border-radius: 20px;
  }
  .notice-bar-container {
    display: flex;
    width: calc(100% - 30px);
    height: 20px;
    overflow: hidden;
    margin-left: 5px;
  }
  .notice-img {
    margin-left:10px;
    width: 20px;
    height: 20px;
  }
  .notice-bar__wrap {
    margin-left: 10px;
    display: flex;
    animation: move 30s linear infinite;
    line-height: 20px;
    color: #000;
   
    .notice-bar__wrap_text {
      width: max-content;
      min-width: 100px;
    }
  }
  @keyframes move {
    0% {
      transform: translateX(100%);
    }
    100% {
      transform: translateX(-100%);
    }
  }
  </style>