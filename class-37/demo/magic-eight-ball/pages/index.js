import Head from 'next/head'
import Link from 'next/link'

import { useState } from 'react';



export default function Home() {

  const [answeredQuestions, setAnsweredQuestions] = useState([]); // Define the hook

  function questionHandler(event){
    event.preventDefault();
    let replies = ['yes', 'no', 'maybe', 'cat', 'school', 'here we go'];
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
    <div className="">
      <Head>
        <title>Magic 8 Ball</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      
      <header className="flex justify-between bg-red-400 text-gray-100 p-4 items-center">
        <h1 className="text-4xl">Magic 8 Ball</h1>
        {/* Use the state "reply" */}
        <p>{answeredQuestions.length} questions answered</p>
        
      </header>

      <main className="">
        <form className="flex w-1/2 bg-gray-200 mx-auto my-4 p-2" onSubmit={questionHandler}>
          <input name="question" className="flex-auto p-2"/>
          <button className="px-4 py-1 mx-2 bg-gray-500 rounded-full text-gray-100">Ask</button>
        </form>
        <div className="w-96 h-96 mx-auto my-4 bg-gray-900 rounded-full">
            <div className="relative flex items-center justify-center w-48 h-48 rounded-full bg-gray-200 top-16 left-16">
                {/* Use the state "reply" */}    
                <p className="text-xl text-center">{getMostRecentReply()}</p>
            </div>
        </div>
        <table className="w=1/2 mx-auto my-4">
          <thead>
            <tr>
              <th className="border border-blue-600">No.</th>
              <th className="border border-blue-600">Quesiton</th>
              <th className="border border-blue-600">Response</th>
            </tr>
          </thead>
          <tbody>
            {
              answeredQuestions.map(item => {
                return(
                  <tr>
                    <td className="border border-blue-600">{item.id}</td>
                    <td className="border border-blue-600">{item.question}</td>
                    <td className="border border-blue-600">{item.reply}</td>
                  </tr>
                )
              })
            }
            
          </tbody>
        </table>
      </main>
    
      <footer className="bg-red-400 text-gray-100 p-4 items-center">
        <Link href="/careers">
          <a>Careers</a>
        </Link>
      </footer>
    </div>
  )
}
