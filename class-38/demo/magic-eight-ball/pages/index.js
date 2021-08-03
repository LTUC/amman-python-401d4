import Head from 'next/head'

import { useState } from 'react';
import {replies} from '../data.js';

import Header from '../components/header.js';
import QuestionsForm from '../components/QuestionsForm.js';
import EightBall from '../components/EightBall.js';
import QuestionsTable from '../components/QuestionsTable.js';

export default function Home() {

  // Hooks and States
  // const [reply, setReply] = useState(''); 
  // const [counter, setCounter] = useState(0);

  const [answeredQuestions, setAnsweredQuestions] = useState([]); // Define the hook

  function questionHandler(event){
    event.preventDefault();
    const randomReply = replies[Math.floor(Math.random() * replies.length)];

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

      </main>

    </>
  )

}
