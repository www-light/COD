<template>
    <!-- 问题页面 -->
    <section v-show="activeSection === 'question'" id="question" class="game">
        <div class="part1">
            <img src="\logo2.png" alt="Animal" class="animal-image">
            <div style="padding-top: 80px;" >
                <button @click="alternateImage" class="submit-button">换道题 ⇵</button>
                <button @click="seeAnswer" class="submit-button" style="margin-left:30px;">看答案 ☛</button>
            </div>
        </div>
        <div class="part2">
            <div class="buttom">
                <div class="buttom-1">
                    <h3 style="margin:0px; font-size: 130%;">请写下您的答案：</h3> 
                    <input type="text" v-model="guess" placeholder="input your anwser..." class="guess-input">  
                    <button @click="checkGuess" class="submit-button">Submit</button>
                </div>
                <div class="buttom-2">
                    <div class="prompt-1"><h3>提示💡</h3></div>
                    <div class="prompt-2">
                        <p>Think harder! It has four legs and a tail.</p>
                        <p style="margin-top: 0px;">注意: 请输入例如dog, cat等简单动物名即可</p>
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
        <button @click="backQestion" style="height: 30px;">回到上层</button>
    </section>

</template>

<script>
export default {
    data() {  
        return {  
        guess: '',  
        activeSection:'question',  
        hint: 'Think harder! It has four legs and a tail.',  
        correctAnswer: 'Dog' // 假设正确答案是Dog  
        };  
    },  
    methods: {  
        checkGuess() {  
            if (this.guess.toLowerCase() === this.correctAnswer.toLowerCase()) {  
                alert('恭喜你，回答正确！');     
            } else {  
                alert('抱歉，回答错误。');    
            } 
            this.activeSection = 'answer'; 
        },
        alternateImage() {
            
        }, 
        backQestion() {
            this.activeSection = 'question';
        },
        seeAnswer() {
            this.activeSection = 'answer';
        }
    }         
}
</script>
    
<style scoped>
.game{
    display: flex;
    box-sizing: border-box;
    height: 500px;
    /* border:1px solid black; */
    padding: 0px 250px;
}

.part1 {
    /* border: 3px solid green; */
    width: 40%;
}

.animal-image {  
  width: 300px;  
  height: auto;  
  margin-top: 20%; 
  border:10px solid aliceblue; 
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
  border:1px solid aliceblue;
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
</style>