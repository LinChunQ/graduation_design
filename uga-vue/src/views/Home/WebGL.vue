<template>
  <div ref="container" class="stars-container" @click="createMeteorAtClick"></div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { TextureLoader } from 'three';

const container = ref(null);

// 初始化变量
let scene, camera, renderer, stars = [];
let moon, controls, meteors = [];
let raycaster = new THREE.Raycaster();
let mouse = new THREE.Vector2();



const initThreeJS = () => {
  // 1. 创建场景
  scene = new THREE.Scene();
  
  // 2. 创建相机
  camera = new THREE.PerspectiveCamera(
    75, 
    container.value.clientWidth / container.value.clientHeight, 
    0.1, 
    3000
  );
  camera.position.set(0, 0, 500);
  
  // 3. 创建渲染器
  renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  renderer.setSize(container.value.clientWidth, container.value.clientHeight);
  renderer.setClearColor(0x000000, 1);
  container.value.appendChild(renderer.domElement);
  
  // 4. 添加轨道控制器（可选，方便调试）
  controls = new OrbitControls(camera, renderer.domElement);
  controls.enableZoom = false;
  controls.enablePan = false;
  controls.autoRotate = true;
  controls.autoRotateSpeed = 0.8;
  
  // 5. 创建星星
  createStars();
  
  // 6. 创建月球
  createMoon();
  
  // 7. 添加环境光和平行光
  const ambientLight = new THREE.AmbientLight(0x333333);
  scene.add(ambientLight);
  
  const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
  directionalLight.position.set(1, 1, 1);
  scene.add(directionalLight);
  
  // 8. 添加窗口大小变化监听
  window.addEventListener('resize', handleResize);
};

const createStars = () => {
  // 创建星星几何体
  const geometry = new THREE.BufferGeometry();
  const vertices = [];
  
  // 创建15000颗星星
  for (let i = 0; i < 15000; i++) {
    const x = (Math.random() - 0.5) * 2000;
    const y = (Math.random() - 0.5) * 2000;
    const z = (Math.random() - 0.5) * 2000;
    vertices.push(x, y, z);
  }
  
  geometry.setAttribute('position', new THREE.Float32BufferAttribute(vertices, 3));
  
  // 创建星星材质
  const material = new THREE.PointsMaterial({
    size: 1,
    color: 0xffffff,
    transparent: true,
    opacity: 0.8,
    sizeAttenuation: true
  });
  
  // 创建星星粒子系统
  const starSystem = new THREE.Points(geometry, material);
  scene.add(starSystem);
  
  // 添加一些闪烁的大星星
  const bigStarsGeometry = new THREE.BufferGeometry();
  const bigStarsVertices = [];
  const bigStarsSizes = [];
  
  for (let i = 0; i < 500; i++) {
    const x = (Math.random() - 0.5) * 2000;
    const y = (Math.random() - 0.5) * 2000;
    const z = (Math.random() - 0.5) * 2000;
    bigStarsVertices.push(x, y, z);
    bigStarsSizes.push(Math.random() * 3 + 1);
  }
  
  bigStarsGeometry.setAttribute('position', new THREE.Float32BufferAttribute(bigStarsVertices, 3));
  bigStarsGeometry.setAttribute('size', new THREE.Float32BufferAttribute(bigStarsSizes, 1));
  
  const bigStarsMaterial = new THREE.PointsMaterial({
    size: 2,
    color: 0xffffff,
    transparent: true,
    opacity: 0.8,
    sizeAttenuation: true,
    vertexColors: false
  });
  
  const bigStars = new THREE.Points(bigStarsGeometry, bigStarsMaterial);
  scene.add(bigStars);
  stars.push(bigStars);
};

const createMoon = async () => {
  // 创建月球材质
  const textureLoader = new TextureLoader();
  
  // 加载月球纹理（这里使用Three.js自带的灰度纹理模拟月球表面）
  // 实际项目中可以使用真实的月球贴图
  const moonTexture = await textureLoader.loadAsync('https://raw.githubusercontent.com/mrdoob/three.js/dev/examples/textures/planets/moon_1024.jpg');
  
  // 创建月球材质
  const moonMaterial = new THREE.MeshPhongMaterial({
    map: moonTexture,
    bumpMap: moonTexture,
    bumpScale: 0.05,
    specular: new THREE.Color('grey'),
    shininess: 5
  });
  
  // 创建月球几何体
  const moonGeometry = new THREE.SphereGeometry(50, 64, 64);
  
  // 创建月球网格
  moon = new THREE.Mesh(moonGeometry, moonMaterial);
  moon.position.set(-50, 50, -200);
  
  scene.add(moon);
};
const createMeteorAtClick = (event) => {
  // 获取容器相对于视口的位置
  const rect = container.value.getBoundingClientRect();
  
  // 计算容器内的相对坐标
  const x = event.clientX - rect.left;
  const y = event.clientY - rect.top;
  
  // 转换为标准化设备坐标 (-1 到 +1)
  mouse.x = (x / rect.width) * 2 - 1;
  mouse.y = -(y / rect.height) * 2 + 1;
  // 更新射线投射器
  raycaster.setFromCamera(mouse, camera);
  
  // 计算射线与远处平面的交点
  const distance = 1000; // 从相机到远处平面的距离
  const direction = raycaster.ray.direction.clone().normalize();
  const targetPoint = raycaster.ray.origin.clone().add(direction.multiplyScalar(distance));
  
  // 在点击位置创建流星
  createMeteor(targetPoint);
};

const createMeteor = (startPoint) => {
  // 流星几何体 - 使用锥体模拟流星头部
  const headGeometry = new THREE.ConeGeometry(10, 10, 32);
  
  // 流星材质
  const headMaterial = new THREE.MeshBasicMaterial({ 
    color: 0xfbfd24,
    transparent: true,
    opacity: 0.9
  });
  
  // 创建流星头部
  const head = new THREE.Mesh(headGeometry, headMaterial);
  head.position.copy(startPoint);
  
  // 随机流星方向（稍微向下倾斜）
  const direction = new THREE.Vector3(0
  -80, //x轴
  -10,  //y轴
  1).normalize();
  
  // 将流星添加到场景
  scene.add(head);
  
  // 存储流星数据
  const meteor = {
    head,
    direction,
    speed: 5 + Math.random() * 10,
    life: 100,
  };
  
  meteors.push(meteor);
};
const updateMeteors = () => {
  for (let i = meteors.length - 1; i >= 0; i--) {
    const meteor = meteors[i];
    
    // 更新位置
    meteor.head.position.addScaledVector(meteor.direction, meteor.speed);

    // 减少生命周期
    meteor.life--;
    
    // 如果流星超出视野或生命周期结束，移除它
    if (meteor.life <= 0 || 
        meteor.head.position.length() > 2000) {
      scene.remove(meteor.head);
      meteors.splice(i, 1);
    }
  }
};
const animate = () => {
  requestAnimationFrame(animate);
  
  // 让星星缓慢旋转
  stars.forEach(starGroup => {
    starGroup.rotation.x += 0.0001;
    starGroup.rotation.y += 0.0001;
  });
  
  // 更新流星
  updateMeteors();
  
  // 更新控制器
  if (controls) {
    controls.update();
  }
  
  renderer.render(scene, camera);
};

const handleResize = () => {
  camera.aspect = container.value.clientWidth / container.value.clientHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(container.value.clientWidth, container.value.clientHeight);
};

onMounted(() => {
  initThreeJS();
  animate();
});

onBeforeUnmount(() => {
  if (renderer) {
    renderer.dispose();
  }
  if (controls) {
    controls.dispose();
  }
  window.removeEventListener('resize', handleResize);
});
</script>

<style scoped>
.stars-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 0;
  overflow: hidden;
  pointer-events: auto;
}
</style>