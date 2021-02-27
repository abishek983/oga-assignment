const express = require('express');
const app = express();
const bodyParser = require("body-parser")

const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Set EJS as templating engine 
app.set('view engine', 'ejs');

app.use(bodyParser.urlencoded({
    extended:true
}));

let serverInput, score = 0
let life = 3 

app.get('/', (req, res) => {
    //showing winnig page if score > 10
    if(score>=10)
        res.render("won")
    //showing losing page if no life left or score < -3
    if(score <= -3 || life <=0)
        res.render("lose")
    else{
        rl.question("Enter character to show to client ", (character) => {
            serverInput = character
            res.render("home", {character:character, score: score, life: life})
            // rl.close()
        })
    }
});

app.post('/', (req,res) => {
    const userInput = req.body.userInput
    if(userInput === serverInput){
        score++;
    }
    //no user input
    else if(userInput === undefined){
        life--;
    }
    else{
        score--;
    }
    res.redirect('/')
})

const server = app.listen(8000,  () =>  {
    console.log('listining to port 8000')

}); 
