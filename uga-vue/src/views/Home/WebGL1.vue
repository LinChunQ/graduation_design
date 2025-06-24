<template>
<div ref="container" class="webgl1"></div>
</template>

<script setup>
import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

const container = ref(null);
//初始化场景，相机，渲染器
let scene, camera, renderer;
//初始化轨道控制器方便调试
let controls;

const initThreeJS  = () => { 
    //1、创建场景
    scene = new THREE.Scene();
    scene.background = new THREE.Color(0x000000); // 设置黑色背景

    //2、创建相机
    camera = new THREE.PerspectiveCamera(
     75, //视角75度(fov=Filed for view )
     window.innerWidth / window.innerHeight, //定义渲染画面的宽高比(aspect)
     0.1,//定义相机能看到的最近距离。比 near 更近的物体不会被渲染。
     1000 //定义相机能看到的最远距离。比 far 更远的物体不会被渲染。
    );
    camera.position.z = 5; //设置相机的位置

    //3、创建渲染器
    renderer = new THREE.WebGLRenderer({
        antialias: true, //开启抗锯齿
        alpha: false //设置渲染器是否可以透明
    });
    renderer.setSize(window.innerWidth, window.innerHeight); //设置渲染器的输出画布（<canvas>）的宽度和高度，通常与容器（如 div）的尺寸一致。
    renderer.setClearColor(0x000000, 0);    //设置渲染器清除画布时使用的背景颜色和透明度。
    container.value.appendChild(renderer.domElement);   //将渲染器的画布（renderer.domElement，即 <canvas> 元素）插入到指定的 HTML 容器

    //4、添加轨道控制器
    controls = new OrbitControls(camera, renderer.domElement);//将相机（camera）和渲染器的画布（renderer.domElement）绑定到控制器。
    controls.enableZoom = false;
    controls.enablePan = false;
    controls.autoRotate = false; //设置自动旋转
    controls.autoRotateSpeed = 0.8;

    // 5、添加立方体
    createCube();

    //  6、添加辅助坐标轴
    const axesHelper = new THREE.AxesHelper(5); 
    scene.add(axesHelper);

    // 7、添加环境光和平行光
    const ambientLight = new THREE.AmbientLight(0x333333);
    scene.add(ambientLight);
    const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
    directionalLight.position.set(1, 1, 1);
    scene.add(directionalLight);

    // 8、添加窗口大小变化监听
    window.addEventListener('resize',handleResize);
    //9、最后渲染
    animate();
}
// 添加动画循环
function animate() {
    //浏览器原生 API，以屏幕刷新率（通常 60 FPS）递归调用 animate 函数，实现平滑动画。
    requestAnimationFrame(animate);
    //OrbitControls 需要在每一帧更新内部状态（如惯性、阻尼效果），否则交互会失效。
    controls.update();
    //将当前场景（scene）和相机视角（camera）结合，输出到渲染器的画布上。
    renderer.render(scene, camera);
}
//定义立方体
function createCube() {
  // const cube = new THREE.Mesh(
  //   new THREE.BoxGeometry(1, 1, 1),
  //   new THREE.MeshBasicMaterial({ color: 0x00ff00 })
  // );
  // scene.add(cube); 
const geometry = new THREE.BufferGeometry();
const vertices = new Float32Array( [
	-1.0, -1.0,  1.0, // v0
	 1.0, -1.0,  1.0, // v1
	 1.0,  1.0,  0, // v2
	-1.0,  1.0,  0, // v3
   1.0,    0,  -1.0, // v4
] );
const indices = new Uint16Array([0, 1, 2, 0, 2, 3]);

geometry.setAttribute('position', new THREE.BufferAttribute(vertices, 3));
geometry.setIndex(new THREE.BufferAttribute(indices, 1)); // 关键：设置索引

const material = new THREE.MeshBasicMaterial( { color: 0xff0000 } );
const mesh = new THREE.Mesh( geometry, material );
scene.add( mesh );
}
//处理窗口大小变化
const handleResize = () => {
  camera.aspect = container.value.clientWidth / container.value.clientHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(container.value.clientWidth, container.value.clientHeight);
};


onMounted(() => {
    initThreeJS();
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

<style scoped lang="scss">
.webgl1{
    width: 100%;
    height: 100%;

}
</style>