<template>
  <div class="not-found">
    <h1>404</h1>
    <p>页面未找到</p>
    <img src="@/assets/images/404.png" alt="404 Not Found" class="not-found-image">
    <router-link to="/" class="back-home">返回首页</router-link>
  </div>
</template>

<script>
export default {
  name: 'NotFound'
};
</script>

<style scoped>
.not-found {
  text-align: center;
  padding: 50px;
  font-size: 2rem;
  color: #333;
}

.not-found h1 {
  font-size: 5rem;
  margin-bottom: 20px;
  color: #ff6b6b;
}

.not-found p {
  font-size: 1.5rem;
  margin-bottom: 40px;
}

.not-found-image {
  max-width: 100%;
  height: auto;
  margin-bottom: 40px;
}

.back-home {
  display: inline-block;
  padding: 10px 20px;
  background-color: #ff6b6b;
  color: white;
  text-decoration: none;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.back-home:hover {
  background-color: #ff4c4c;
}
</style>