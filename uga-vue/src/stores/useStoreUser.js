import { defineStore } from "pinia"
import { reactive, ref, computed } from 'vue'
import {getUserInfoData,requestGrading,editUserInfo,
        createCourse,getCourseById,deleteCourseById,
        updateCourse,getTestByCourseId} from '@/apis/user.js'
import { ElMessage } from 'element-plus'

const useUserStore = defineStore('useUserStore', () => {
  //用户基本信息
  const userInfo = reactive({
    username: '',
    sex: '',
    age: '',
    email: '',
    phone: '',
    address: '',
    school: '',
    profession: ''
  })

  const courseInfo=reactive({
    course_id:'',
    course_name:'',
    teacher_id:'',
    stu_count:0,
    submit_count:0,
    idDelete:false
  })

  const courseList=reactive([])
  const testPaperData=reactive({})
  //单个试卷分数
  const singleGrade=ref({})
  async function getUserInfo(){
    const res=await getUserInfoData()
    Object.assign(userInfo,res.userInfo)
    localStorage.setItem('userInfo',JSON.stringify(res.userInfo))
    
  }

  async function updateUserInfo(data){
     await editUserInfo(data)
  }
  async function smartGrading(data){
    const res= await requestGrading(data)
    singleGrade.value=res;
  } 
  
  async function addCourse(data){
     await createCourse(data)
  }

  async function getCourse(){
    const res=await getCourseById();
   Object.assign(courseList,res)
  }

  async function deleteCourse(data){
    await deleteCourseById(data)
  }

  async function editCourse(data){
    await updateCourse(data)
  }

  async function getTestPaper(data){
    const res=await getTestByCourseId(data)
    if(res.length!=0){
      Object.assign(testPaperData,res)
    }else{
      testPaperData.length=0;
    }
   
  }

  return {
    userInfo,
    singleGrade,
    editUserInfo,
    courseList,
    testPaperData,
    getUserInfo,
    smartGrading,
    updateUserInfo,
    addCourse,
    getCourse,
    deleteCourse,
    editCourse,
    getTestPaper
  }
},{persist:true})

export default useUserStore