<template>  
    <div class="home">
      <div class="title">
        <h1 style="font-size:300%">欢迎浏览我们的网站<br>这里汇聚了关于如何保护野生动物的信息。</h1>
        <h1 style="font-size:200%">保护动物,人人有责</h1>  
      </div>
      <div class="logo">
        <img src="\logo.jpg" alt="logo"/>
      </div>
    </div> 

    <hr class="hr-edge-weak">

    <div class="intro">
      <div class="introp">
        <img src="\logo1.jpg" alt="logo1">
      </div>
      <div class="introt">
        <h1 style="font-size:200%">野生动物保护的重要性</h1>
        <h1 style="font-size:160%">由于物种以前所未有的速度减少以及生物多样性面临的威胁不断升级，
          动物保护的紧迫性已成为全球迫切关注的问题。</h1>
        <h1 style="font-size:160%">人类活动（包括森林砍伐、城市化和农业扩张）破坏和破坏了自然栖息地。
          减少了许多物种的可用生存空间，导致种群数量下降并限制了它们繁衍生息的能力。</h1>
      </div>
    </div>

      <hr class="hr-edge-weak">

    <div class="link">
      <div class="linkt">
        <h1 style="font-size:200%">关于我们所实现的小型隐蔽动物识别</h1>
        <h1 style="font-size:160%">小型隐蔽野生动物的识别在生态保护中具有重要意义。由于它们通常难以被发现，
          但却在生态系统中扮演着关键角色，识别这些动物有助于了解生态链的完整性及其健康状况。
          这样可以更好地监控生物多样性，及时发现环境问题，并采取措施保护这些隐蔽物种和它们的栖息地。</h1>
        <router-link to="/detect" style="font-size: 150%;">👉click here to have a try</router-link>
      </div>

       <div class="linkp">
        <img src="\logo2.png" alt="logo2">
       </div>
    </div>  

</template>  
    
<script>
export default{ 
    // 变量
    data(){
      return{
      }
    },
    // 函数
    methods: {   
    } ,
    // 组件
    components:{
    }
  }  
</script>  

<style scoped>  
  .home {  
    text-align: left;  
    padding: 20px; 
    margin: 10px;
    /* width: 1600px; */
    display: flex;
    justify-content: center;
  }  
  .title{  
    text-align: left;  
    padding: 70px 0px 20px 140px;  
    margin: 10px;
    box-sizing: border-box;
    width: 700px;
    display:inline-block;
    background: linear-gradient(to right, rgb(2, 74, 10), rgb(154, 249, 180));
    -webkit-background-clip: text;
    color: transparent;
  }
  .logo{
    margin:10px;
    width: 700px;
    margin: 20px;
    display:inline-block;
  }
  .intro{
    /* width:1600px; */
    padding-left: 125px;
  }
  .introp{
    width:600px;
    display:inline-block;
    vertical-align:bottom;
  }
  .introt{
    width:600px;
    padding: 20px;
    display:inline-block;
    vertical-align:bottom;
    background-color:forestgreen;
    /* background-color:#42b983; */
    color:aliceblue;
  }
  .link{
    margin-bottom: 30px;
    padding-right: 100px;
  }
  .linkp{
    width:600px;
    display:inline-block;
    vertical-align:bottom;
  }
  .linkt{
    width:600px;
    padding: 30px;
    display:inline-block;
    vertical-align:bottom;
    /* background-color:rgb(126, 175, 93); */
    background-color:#42b983;
    color:aliceblue;
  }

  .hr-edge-weak {
		border: 0;
    margin: 30px 0px;
		padding-top: 1px;
		background: linear-gradient(to right, transparent, #d0d0d5, transparent);
	}

</style>