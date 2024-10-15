<template>
    <!-- 问题页面 -->
    <section v-show="activeSection === 'question'" id="question" class="game">
        <div class="part1">
            <img :src=animal.animals_skeletion_image alt="Animal" class="animal-image">
            <div style="padding-top: 45px;" >
                <button @click="alternateAnimal" class="submit-button">换道题 ⇵</button>
                <button @click="seeAnswer" class="submit-button" style="margin-left:30px;">看答案 ☛</button>
            </div>
        </div>
        <div class="part2">
            <div class="buttom">
                <div class="buttom-1">
                    <h3 style="margin:0px; font-size: 130%;">请写下您的答案：</h3> 
                    <input type="text" v-model="user_input" placeholder="input your anwser..." class="guess-input">  
                    <button @click="submitInput" class="submit-button">Submit</button>
                </div>
                <div class="buttom-2">
                    <div class="prompt-1"><h3>提示💡</h3></div>
                    <div class="prompt-2">
                        <p>{{ animal.problem_info }}</p>
                        <p style="margin-top: 0px;">注意: 请输入例如猕猴, 猫头鹰环蝶等简单动物名即可</p>
                    </div>
                </div>
            </div>
            <div class="title">
                <h1>Guess who am I ?</h1>
            </div>
        </div>  
    </section>

    <!-- 结果页面 -->
    <section v-show="activeSection === 'answer'" id="answer" class="game">
        <button @click="backQestion" style="height: 30px;width: 100px;">回到上层</button>
        <img :src="answerAnimalImage" alt="Animal in Answer Page" class="animal-image-answer" />
    
        <div class="parent-container">
            <div class="name-container">
                <h2>My name is</h2>
                <div style="font-size: 30px; font-weight: bold;" class="parentDiv">
                    <p>{{ animalName }}  !</p>
                </div>
            </div>
            <div class="answer-info-box">
                <h3>答案 ❕</h3>
            </div>
            <div class="answer-info-text">
                <p>{{ answerInfoText }}</p>
            </div>
        </div>
        
        <p class="thank-you-message">Thank you for experiencing this game🎉. <br>Hope you have gained fun and knowledge in the wonderful world of animals.</p>
          
    </section>
    

</template>

<script>
import axios from 'axios'

export default {
    data() {  
        return {  
            // 用户输入
            user_input: '',  
            activeSection:'question',
            // 动物对象   
            animal: {
                problem_number:'',
                problem_info: '暂未开始游戏，请打开后端服务器',
                animals_info: '',
                animals_name: '',
                animals_origin_image: '',
                animals_skeletion_image: 'example3r.jpg',
                animals_skeleton_image_url:  '',
            },
            answerAnimalImage: '', 
             answerInfoText: '',
             animalName: ''
        };  
    }, 
    created(){
        this.getRandomAnimal();
    },
    methods: { 
        // 提交用户答案
        async submitInput() {
            try {
                const formData = new FormData();
                formData.append('user_input', this.user_input);
                formData.append('image_name',this.animal.animals_skeleton_image_url);
                const response = await axios.post('http://localhost:8000/api/check_animal_name/',formData,
                    {
                        headers: {  'Content-Type': 'multipart/form-data'  }
                    }
                );
            
                // 处理后端返回的结果  
                if (response.data.result) {  
                    alert('恭喜你，回答正确！');  
                } else {  
                    alert('抱歉，回答错误。');  
                }
            } catch (error) {  
            console.error('发送请求时出错:', error);  
            } 
            this.seeAnswer() 
        } ,
        // 请求动物对象
        async getRandomAnimal() {  
            try {  
                const response = await axios.get('http://localhost:8000/api/random_animal');  
                this.animal = response.data;
                //解码base64图片,及结果界面调用信息
                this.animal.animals_skeletion_image = `data:image/jpeg;base64,${response.data.animals_skeletion_image}`;
                this.animal.animals_origin_image = `data:image/jpeg;base64,${response.data.animals_origin_image}`;
                this.answerInfoText = this.animal.animals_info;
                this.animalName = this.animal.animals_name;
            } catch (error) {  
                console.error('Error fetching random animal:', error);  
                // 可以在这里处理错误，例如显示一个错误消息  
            } 
            //清空input
            this.user_input = ''; 
        } , 
        // 更换动物对象
        alternateAnimal() {
            this.getRandomAnimal();
        }, 
        // 回到问题页面
        backQestion() {
            this.activeSection = 'question';
            this.getRandomAnimal();
        },
        // 跳转答案页面
        seeAnswer() {
    this.activeSection = 'answer';
    this.answerAnimalImage = this.animal.animals_origin_image;
},
    }         
}
</script>
    
<style scoped>

.game{
    display: flex;
    box-sizing: border-box;
    height: 500px;
    /* border:1px solid black; */
    padding: 0px 225px;
    
}

.part1 {
    /* border: 3px solid green; */
    width: 40%;
}

.animal-image {  
  width: 350px;  
  height: auto;
  height: 250px;  
  margin-top: 20%; 
  border:5px solid aliceblue; 
  border-radius: 5px;
  box-shadow: 0px 0px 15px 10px rgba(0, 0, 0, 0.6);
}

.part2 {
    /* border: 1px solid red; */
    width: 60%;
}

.buttom {
    height: 65%;
    /* border: 1px solid black; */
}

.buttom-1 {
    text-align: left;
    padding: 70px 100px 20px 100px;
    /* border:3px solid blue; */
}

.guess-input {  
  margin: 10px 0px;
  padding: 10px;  
  font-size: 16px;  
  border-radius: 5px;
  border:1px solid grey;
  box-shadow: 0px 0px 15px 2px rgba(0, 0, 0, 0.5);
}  
.submit-button {  
  padding: 10px 20px;  
  font-size: 16px;  
  cursor: pointer;
  border-radius: 5px;
  border:1px solid aliceblue; 
  box-shadow: 0px 0px 15px 2px rgba(0, 0, 0, 0.5);
  margin-left: 3px; 
}
.submit-button:hover {
   background-color: rgb(110, 110, 110);
}  

.buttom-2 {
    text-align: left;
    padding: 0px 100px 20px 100px;
    /* border:3px solid rgb(255, 0, 0); */
}

.prompt-1 {
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #42b983;
    width: 100px;
    height: 40px;
    /* border: 1px solid aliceblue; */
}

.prompt-2 {
    display: grid;
    align-items: center;
    justify-content: center;
    /* height: 100px; */
    width: 400px;
    padding: 0px 20px;
    border: 3px solid #42b983;
}

.title {
    /* border:3px solid rgb(242, 255, 0); */
    height: 35%;

    display: flex; 
    align-items: center;
    justify-content: center;
    font-size: 250%;
}

.hint-box {  
  padding: 10px;  
  background-color: #f0f0f0;  
  border: 1px solid #ddd;  
  margin-top: 10px;  
  text-align: center;  
}  

.animal-image-answer {  
    width: 350px;
    height: 250px;
    margin-top: 8%;
    margin-left: -80px;
    border: 5px solid aliceblue;
    border-radius: 5px;
    box-shadow: 0px 0px 15px 10px rgba(0, 0, 0, 0.6);
    
    
}

.parent-container {
    position: relative;
    
}

h2 {
    position: absolute;
    top: 50px;
    left: 130px;
    letter-spacing: 2px;
    font-size: 40px;
}

.name-container {
    display: flex;
    align-items: center;
}



.parentDiv {
    margin-top: 45px;
    margin-left: 390px;
    letter-spacing: 4px;
}

.parentDiv p {
    font-size: 36px; 
    font-weight: bold;
    letter-spacing: 4px;
}

.answer-info-box {
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #42b983;
    width: 100px;
    height: 40px;
    margin-top: -10px;
    margin-left: 130px;
}

.answer-info-text {
    display: grid;
    align-items: center;
    justify-content: center;
    width: 400px;
    height: 150px;
    padding: 0px 20px;
    border: 3px solid #42b983;
    text-align: justify;
    line-height: 1.5;
    margin-left: 130px;
}


.thank-you-message {
    font-size: 19px;
    font-weight: normal;
    letter-spacing: 2px;
    line-height: 1.8;
    text-align: center; 
    width: 90%;
    position: absolute;
    bottom: 28%;
    left: 20px;
    transform: translateY(72%);
    padding: 20px;
    white-space: nowrap;
}

</style>