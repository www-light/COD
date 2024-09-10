<!-- 模态框组件 -->
<template>
    <!-- 模态框 --> 
    <div  class="modal-overlay">  
        <div class="modal">
            <!-- 推出按钮 × -->
            <span class="close" @click="closeModel">&times;</span>
            <!-- 图像内容 -->
            <img :src="imgUrl" alt="大图" class="modal-content" id="img">     
        </div>  
    </div>  
</template>

<script>
    export default{
      data(){
        return{

        }
      },
        props:{
            imgUrl:String,
        },
        methods:{
            closeModel(){
                this.$emit("ModelEvent")
            }
        }
    }
</script>

<style scoped>
/*------- 模态框样式 ------*/
/* 模态框背景 */  
.modal-overlay {  
  position: fixed;  
  top: 0;  
  left: 0;  
  width: 100%;  
  height: 100%;  
  background-color: rgba(0, 0, 0, 0.5);  
  display: flex;  
  justify-content: center;  
  align-items: center; 
  z-index: 200; 
}  

/* 模态框内容 */  
.modal {  
  background-color: #000000;  
  border: 1px solid #888;  
  /* width: 80%;   */
  width: 800px;  
  padding: 5px;    /* 白边 */
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);  
  position: relative;  
}  

/* 关闭按钮 */  
.close {  
  position: absolute;  
  top: 5px;  
  right: 25px;  
  color: #bfbfbfe7;  
  font-size: 40px;  
  font-weight:normal;  
  cursor: pointer;  
}  

.close:hover,  
.close:focus {  
  color: #665f5f;  
  text-decoration: none;  
  cursor: pointer;  
}  

/* 模态框图片 */  
.modal-content {  
  width: 800px;  
  max-height: 80vh; /* 防止图片过高 */  
  object-fit: contain; /* 保持图片比例 */ 
} 
</style>