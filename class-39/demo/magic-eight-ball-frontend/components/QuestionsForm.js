export default function QuestionsForm(props){
    return(
      <form className="flex w-1/2 bg-gray-200 mx-auto my-4 p-2" onSubmit={props.questionHandler}>
        <input name="question" className="flex-auto p-2"/>
        <button className="px-4 py-1 mx-2 bg-gray-500 rounded-full text-gray-100">Ask</button>
      </form>
    );
  }