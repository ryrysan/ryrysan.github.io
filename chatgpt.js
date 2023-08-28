const OpenAI = require("openai");
require('dotenv').config({path:'/Users/ryanlee/dev/ryrysan.github.io/process.env'})

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});
const openFun = async() => {
const chatCompletion = await openai.chat.completions.create({
    model: "gpt-3.5-turbo",
    messages: [{"role": "user", "content": "explain how to solve 4 + 7 to a beginner in math"}],
    max_tokens:200
  });

  console.log(chatCompletion.choices[0].message);
}

openFun();