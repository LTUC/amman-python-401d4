export default function Header(props){
    return(
      <header className="flex justify-between bg-red-400 text-gray-100 p-4 items-center">
        <h1 className="text-4xl">{props.title}</h1>
        {/* Use the state "reply" */}
        <p>{props.answers.length} questions answered</p>
      </header>
    );
  }
  