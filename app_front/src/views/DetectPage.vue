<template>  
  <div id="all">

    <div style="display: flex; padding:10px 0;">
      <div style="font-size: 110%;"><h1>Begin to detect aninmals` images</h1></div>
    </div>

    <div style="display: flex;">

      <div style="border: 1px solid white; width: 430px;">
        <div><img :src="imgUrl" alt="点击查看大图" @click="showModel[3] = true" style="width: 400px; height: 330px;"></div>
        <div style="padding-top: 20px; font-size: 120%">
              <button :class="srcButton[3]?'srcdown':'srcup'" @click="clickSrc(3)">src</button>
              <button :class="resButton[3]&&resimgUrl!=''?'resdown':'resup'" @click="clickRes(3)">res</button>
        </div>
        <div style="border: 1px solid white; text-align: center;">
          <h3>上传动物照片</h3> 

            <input type="file" @change="onFileChange" accept="image/*">
            
            <button @click="uploadPhoto">上传</button> 
            <p>Message: {{ uploadMessage }}</p>

            <!-- 图片 -->
            <div v-if="imgUrl">
              <!-- 缩略图 -->
              <!-- 模态框组件 需要条件，传Url，监听关闭事件-->
              <ShowModal v-if="showModel[3]" :imgUrl="imgUrl"  @ModelEvent="showModel[3] = false"/>
            </div> 
        </div>
      </div>

      <div style="border: 1px solid white">

        <div style="display: flex;">
          <div style="padding:0 30px 10px 0px;" >
            <img :src="Example[0]" alt="点击查看" style="width: 200px; height: 150px;" @click="showModel[0]=true">
          </div>
          <div style="padding-top: 20px; font-size: 120%">
            <div>small-size bird<br>小型鸟类</div>
            <div style="padding-top: 20px; font-size: 120%">
              <button :class="srcButton[0]?'srcdown':'srcup'" @click="clickSrc(0)">src</button>
              <button :class="resButton[0]?'resdown':'resup'" @click="clickRes(0)">res</button>
            </div>
          </div>
          <div v-if="showModel[0]">
            <ShowModal v-if="showModel[0]" :imgUrl="Example[0]"  @ModelEvent="showModel[0] = false"/>
          </div> 
        </div>

        <div style="display: flex;">
          <div style="padding:0 30px 10px 0px;">
            <img :src="Example[1]" alt="点击查看" style="width:200px; height: 150px;" @click="showModel[1]=true"> 
          </div>
          <div style="padding-top: 20px; font-size: 120%">
            <div>spider 山蛛</div>
            <div style="padding-top: 20px; font-size: 120%">
              <button :class="srcButton[1]?'srcdown':'srcup'" @click="clickSrc(1)">src</button>
              <button :class="resButton[1]?'resdown':'resup'" @click="clickRes(1)">res</button>
            </div>
          </div>
          <div v-if="showModel[1]">
              <ShowModal v-if="showModel[1]" :imgUrl="Example[1]"  @ModelEvent="showModel[1] = false"/>
          </div>
        </div>

        <div style="display: flex;">
          <div style="padding:0 30px 10px 0px;">
            <img :src="Example[2]"  alt="点击查看" style="width:200px; height: 150px;" @click="showModel[2]=true">
          </div>
          <div style="padding-top: 20px; font-size: 120%">
            <div>sea turtle 海龟</div>
            <div style="padding-top: 20px; font-size: 120%">
              <button :class="srcButton[2]?'srcdown':'srcup'" @click="clickSrc(2)">src</button>
              <button :class="resButton[2]?'resdown':'resup'" @click="clickRes(2)">res</button>
            </div>
          </div>
          <div v-if="showModel[2]">
              <ShowModal v-if="showModel[2]" :imgUrl="Example[2]"  @ModelEvent="showModel[2] = false"/>
          </div>
        </div>

      </div>

    </div>
    
  </div>
  
</template>  
  
<script>  
import axios from 'axios';  
// 导入模态框组件
import ShowModal from '../components/ShowModel.vue'
import ShowModel from '../components/ShowModel.vue';
  
export default {  
  name: 'UploadPhoto',  
  data() {  
    return { 
      selectedFile: "",
      srcimgUrl:"/example.jpg",
      resimgUrl:"",  
      imgUrl:"/example.jpg",
      uploadMessage: '暂未上传',
      // 控制模态框显示与隐藏  
      showModel: [false,false,false,false], 
      
      srcButton:[true,true,true,true],
      resButton:[false,false,false,false],
      Example:['/example1.jpg','/example2.jpg','/example3.jpg'],
    }; 
  },
  components:{
    // 加载模态框组件
    ShowModal,
  } , 
  methods: {  
    onFileChange(e) {  
      this.selectedFile = e.target.files[0];
      if(!this.selectedFile){
        return;
      }
      // 设置URL
      this.srcimgUrl = URL.createObjectURL(this.selectedFile);
      this.imgUrl=this.srcimgUrl;
      this.resimgUrl='';
      this.uploadMessage = '暂未上传'
    },

    async uploadPhoto() {  
      if (!this.selectedFile) {  
        return;  
      }  
      const formData = new FormData();  
      formData.append('image', this.selectedFile);  
      try { 
        this.uploadMessage = '上传中...' 
        const response = await axios.post('http://localhost:8000/api/upload_images', formData, {  
          headers: {  
            'Content-Type': 'multipart/form-data'  
          }  
        });  
        // this.imgUrl = response.data.image;
        this.resimgUrl = `data:image/jpeg;base64,${response.data.image}`;
        this.imgUrl=this.resimgUrl;
        this.clickRes(3);

        this.uploadMessage = '上传成功！';  
      } catch (error) {  
        console.error('Error uploading file:', error);  
        this.uploadMessage = '上传失败，请重试。';  
      }  
    },

    clickSrc(d){
      this.srcButton[d]=true;
      this.resButton[d]=false;
      if(d==0) this.Example[d]='/example1.jpg';
      if(d==1) this.Example[d]='/example2.jpg';
      if(d==2) this.Example[d]='/example3.jpg';
      if(d==3) this.imgUrl=this.srcimgUrl;
    },

    clickRes(d){
        this.srcButton[d]=false;
        this.resButton[d]=true;
        // 如果大图预览 没有上传得出结果的话，按钮不变
        if(d==3&&this.resimgUrl==""){
          this.srcButton[d]=true;
          this.resButton[d]=false;
        }  
        
        if(d==0) this.Example[d]='/example1r.jpg';
        if(d==1) this.Example[d]='/example2r.jpg';
        if(d==2) this.Example[d]='/example3r.jpg';
        // 大图预览并且得出结果
        if(d==3&&this.resimgUrl){
          this.imgUrl=this.resimgUrl;
        }
    },
  },  
}  
</script>  
  
<style scoped> 
/* 盒子样式 */
#all {  
  text-align: left; 
  padding:20px 325px;
  border: 1xp solid white;   
} 

/* 图片样式 */
#preview{
  height: 300px;
  width: 350px;
  object-fit: contain; /* 保持图片比例 */  
} 

.srcup{
  width:40px;
  height: 20px;
  background-color: rgba(49, 172, 49, 0.5);
  color:rgb(0, 101, 0);
  border:0px;
}

.srcdown{
  width:40px;
  height: 20px;
  background-color: rgb(0, 101, 0);
  color:rgb(255, 255, 255);
  border:0px;
}

.resup{
  margin-left: 10px;
  width:40px;
  height: 20px;
  background-color: rgba(255, 70, 70, 0.5);
  color: rgb(103, 0, 0);
  border:0px;
}

.resdown{
  margin-left: 10px;
  width:40px;
  height: 20px;
  background-color: rgb(103, 0, 0);
  color:rgb(255, 255, 255);
  border:0px;
}
</style>