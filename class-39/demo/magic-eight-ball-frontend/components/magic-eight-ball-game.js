import Head from 'next/head'

import {useState } from 'react';
import { useEffect } from 'react';
import axios from 'axios';

// import {replies} from '../data.js';

import Header from '../components/header.js';
import QuestionsForm from '../components/QuestionsForm.js';
import EightBall from '../components/EightBall.js';
import QuestionsTable from '../components/QuestionsTable.js';
import Footer from '../components/Footer.js';

const baseUrl = 'http://127.0.0.1:8000';
const repliesUrl = baseUrl + '/api/v1/answers/';

export default function MagicEigthBallGame(props) {
  const [answeredQuestions, setAnsweredQuestions] = useState([]); // Define the hook
  const [replies, setReplies] = useState([]); // Replies hook

  function questionHandler(event){
    event.preventDefault();
    const mappedReplies = replies.data.map( (reply) => reply.text);
    const randomReply = mappedReplies[Math.floor(Math.random() * mappedReplies.length)];

    const question = {
      question: event.target.question.value,
      reply: randomReply,
      id:answeredQuestions.length,
    }

    setAnsweredQuestions([...answeredQuestions, question]); // Push the new question to the previous state
    // setReply(randomReply); // set the state of the hook
  }


  function getMostRecentReply(){
    if (answeredQuestions.length == 0){
      return "No questions yet, Ask me please!!"
    }

    return answeredQuestions[answeredQuestions.length - 1].reply;
  }

  // Hook from React to guarantee getRepliesFromAPI will be called first thing in the component
  // Only if there is a token
  // Will be called everytime the token will change
  useEffect( () => {
    if (props.token){
      getRepliesFromAPI();
    }
  }, [props.token]);


  async function getRepliesFromAPI(){

    const config = {headers: {'Authorization': 'Bearer ' + props.token}};
    const answers = await axios.get(repliesUrl, config);
    setReplies(answers);
  }

  

  return (
    <>
      <Head>
        <title>Magic 8 Ball</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      
      {/* Header component */}
      <Header answers={answeredQuestions} title={'Magic 8 Ball'}/>

      <main className="">

        {/* QuestionsForm component */}
        <QuestionsForm questionHandler={questionHandler}/>
        
        {/* EightBall component */}
        <EightBall getMostRecentReply={getMostRecentReply}/>
        
        {/* Table component */}
        <QuestionsTable answeredQuestions={answeredQuestions}/>

        <Footer />

      </main>

    </>
  )

}
